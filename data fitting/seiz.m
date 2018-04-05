%data_2 = readcsv('~/data.csv');

function fit_curve()
data_1 = csvread('.csv');
% Susceptible populations sizes at t = 0
% Data used for fitting 
num_tweets = data_1(:, 1);
times = linspace(0, length(num_tweets) - 1, length(num_tweets));
N = 15000000;
iE = 0;
iI = 10;
iZ = 1;
iS = N -iI -iZ - iE;
ic = [iS iI iE iZ];
% Initial values of the parameters to be fitted 
param0 = [75 0.5 0.5 20 100 100];
% param(1) - beta
% param(2) - p
% param(3) - l
% param(4) - rho
% param(5) - e 
% param(6) - gamma
% Define lower and upper bound for the parameters
large = 10^7;
A = [];
B = [];
LB = zeros(6);
UB = [large 1 1 large large large];
% Setting linear equalities
Aeq = [];
beq = [];
nonlcon = [];
% Declare options for fmincon
options = optimset('Display','iter','MaxFunEvals',Inf,'MaxIter',Inf,...
                       'PlotFcns',{@optimplotfval, @optimplotfunccount});
% Fit the parameters 
[param,E,exitflag] = fmincon(@(param) loss_function(param, times, num_tweets), param0, A, B, Aeq, beq,LB, UB, nonlcon, options);
% Display outputs
ic = param(1:4);
[~, population] = ode23(@(t, population) ...
    RHS(t,population, param(1),param(2),param(3),param(4)...
    , param(5), param(6)),times , ic);
I = population(:,3);
figure();
plot(times, I)
hold on;
scatter(times, num_tweets)
display(E)
for n = 1:8
fprintf('%4.10f\n', param(n))
end
end

% Define loss function
function error = loss_function(param, times, num_tweets)
% Initial conditions for ode solver
ic = param(1:4);
% Solve ode, return population sizes with corresping times
[~, population] = ode23(@(t, population) ...
    RHS(t,population,param(1),param(2),param(3),param(4)...
    , param(5), param(6)),times , ic);
% Select only Infected population size
I = population(:,3);
% Compute error with respect to data
error = norm(I-num_tweets)/norm(num_tweets);
end

% Define differential equation
function dxdt = RHS(t, population, beta, p, l, rho, e, gamma) 
S = population(1); 
I = population(3); 
E = population(2); 
Z = population(4);
N = S + I + E + Z;
dxdt = [-beta*S*(I/N) - gamma*S*(Z/N);
        beta*(1-p)*S*(I/N) - e*E - rho*E*(I/N) + gamma*(1-l)*S*(Z/N);
        beta*p*S*(I/N) + rho*E*(I/N) + e*E;
        gamma*l*S*(Z/N)
    ];
end
