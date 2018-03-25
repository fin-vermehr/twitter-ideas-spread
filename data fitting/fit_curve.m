%data_2 = readcsv('~/data.csv');

function fit_curve()
data_1 = csvread('CambridgeAnalytica.csv');
% Susceptible populations sizes at t = 0
% Data used for fitting 
num_tweets = data_1(:, 1);
times = linspace(0, length(num_tweets) - 1, length(num_tweets));
% Initial values of the parameters to be fitted 
param0 = [3000000 30000 100 36 10 10 60 0.5 0.5 1.7 1 6 0.5];
% param(1) - initial S1
% param(2) - initial S2
% param(3) - Infected population at t = 0
% param(4) - Exposed population at t = 0
% param(5) - Skeptic population at t = 0
% param(6) - beta1
% param(7) - beta2
% param(8) - p
% param(9) - m
% param(10) - e
% param(11) - mu
% param(12) - gamma 
% param(13) - l
% Define lower and upper bound for the parameters
N = param0(1) + param0(2);
large = 10^7;
A = [0 0 0 0 0 1 -1 0 0 0 0 0 0 ];
B = 0;
LB = zeros(13);
UB = [N N N N N large large 1 1 large large large 1];
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
ic = param(1:5);
[~, population] = ode23(@(t, population) ...
    RHS(t,population,param(6),param(7),param(8),param(9),param(10)...
    , param(11), param(12), param(13)),times , ic);
I = population(:,3);
figure();
plot(times, I)
hold on;
scatter(times, num_tweets)
display(E)
display(param)
end

% Define loss function
function error = loss_function(param, times, num_tweets)
% Initial conditions for ode solver
ic = param(1:5);
% Solve ode, return population sizes with corresping times
[~, population] = ode23(@(t, population) ...
    RHS(t,population,param(6),param(7),param(8),param(9),param(10)...
    , param(11), param(12), param(13)),times , ic);
% Select only Infected population size
I = population(:,3);
% Compute error with respect to data
error = norm(I-num_tweets)/norm(num_tweets);
end

% Define differential equation
function dxdt = RHS(t, population, beta1, beta2, p, m, e, mu, gamma, l)
S1 = population(1); 
S2 = population(2); 
I = population(3); 
E = population(4); 
Z = population(5);
N = S1 + S2 + I + E + Z;
dxdt = [-beta1*S1*(I/N) - gamma*S1*(Z/N);
        -beta2*S2*(I/N);
        beta1*(1-p)*S1*(I/N) + beta2*(1-m)*S2*(I/N)...
        + e*E + mu*E*(I/N);
        beta1*p*S1*(I/N) + beta2*m*S2*(I/N)...
        + gamma*l*S1*(Z/N) - mu*E*(I/N) - e*E;
        gamma*(1-l)*S1*(Z/N)
    ];
end
