
%data_2 = readcsv('~/data.csv');

function fit_curve()
data_1 = csvread('AustinBombing.csv');
% Susceptible populations sizes at t = 0
iS2 = 300000;
iE = 0;
iI = 10;
iZ = 0;
ic = [iS2 iI iE iZ];
% Data used for fitting 
num_tweets = data_1(:, 1);
times = linspace(0, length(num_tweets) - 1, length(num_tweets));
% Initial values of the parameters to be fitted 
param0 = [3000000 30 30 30 0.5 0.5 0.5 10 10];
% param(1) - iS1
% param(2) - beta1
% param(3) - beta2
% param(4) - gamma
% param(5) - p
% param(6) - l
% param(7) - m
% param(8) - mu 
% param(9) - e
% Define lower and upper bound for the parameters
large = 10^7;
A = [0 0 0 0 -1 0 1 0 0];
B = 0;
LB = zeros(9);
UB = [large large large large 1 1 1 large large];
% Setting linear equalities
Aeq = [];
beq = [];
nonlcon = [];
% Declare options for fmincon
options = optimset('Display','iter','MaxFunEvals',Inf,'MaxIter',Inf,...
                       'PlotFcns',{@optimplotfval, @optimplotfunccount});
% Fit the parameters 
[param,E,exitflag] = fmincon(@(param) loss_function(param, times, num_tweets,...
    ic), param0, A, B, Aeq, beq,LB, UB, nonlcon, options);
% Display outputs
p0 = [param(1) ic];
[~, population] = ode23(@(t, population) ...
    RHS(t,population,param(2),param(3), param(4), param(5),param(6),param(7),param(8)...
    , param(9)),times , p0);
I = population(:,3);
figure();
plot(times, I)
hold on;
scatter(times, num_tweets)
display(E)
display(param)
end

% Define loss function
function error = loss_function(param, times, num_tweets, ic)
p0 = [param(1) ic];
% Solve ode, return population sizes with corresping times
[~, population] = ode23(@(t, population) ...
    RHS(t,population,param(2),param(3),param(4),param(5),param(6)...
    , param(7), param(8), param(9)),times , p0);
% Select only Infected population size
I = population(:,3);
% Compute error with respect to data
error = norm(I-num_tweets)/norm(num_tweets);
mean_deviation = sum(abs(I - num_tweets))/length(num_tweets);
end

% Define differential equation
function dxdt = RHS(t, population, beta1, beta2, gamma, p, l, m, mu, e)
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
