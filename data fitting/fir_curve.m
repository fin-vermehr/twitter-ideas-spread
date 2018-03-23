
%data_2 = readcsv('~/data.csv');

function fit_curve()
data_1 = csvread('simulated_data.csv');
% Susceptible populations sizes at t = 0
iS1 = 3000000;
iS2 = 30000;
% Data used for fitting 
times = data_1(:, 1);
num_tweets = data_1(:, 2);
% Initial values of the parameters to be fitted 
param0 = [1 1 1 1 1 0.5 0.5 1 1 1 0.5];
% param(1) - Infected population at t = 0
% param(2) - Exposed population at t = 0
% param(3) - Skeptic population at t = 0
% param(4) - beta1
% param(5) - beta2
% param(6) - p
% param(7) - m
% param(8) - e
% param(9) - mu
% param(10) - gamma 
% param(11) - l
% Define lower and upper bound for the parameters
N = iS1 + iS2;
large = 10^7;
A = [0 0 0 1 -1 0 0 0 0 0 0];
B = 0;
LB = zeros(11);
UB = [N N N large large 1 1 large large large 1];
% Setting linear equalities
Aeq = [];
beq = [];
nonlcon = [];
% Declare options for fmincon
options = optimset('Display','iter','MaxFunEvals',Inf,'MaxIter',Inf,...
                       'PlotFcns',{@optimplotfval, @optimplotfunccount});
% Fit the parameters 
[param,E,exitflag] = fmincon(@(param) loss_function(param, times, num_tweets,...
    iS1, iS2), param0, A, B, Aeq, beq,LB, UB, nonlcon, options);
% Display outputs
display(param)
display(E)
display(exitflag)
end

% Define loss function
function error = loss_function(param, times, num_tweets, iS1, iS2)
% Initial conditions for ode solver
ic = [iS1 iS2 param(1:3)];
% Solve ode, return population sizes with corresping times
[~, population] = ode23(@(t, population) ...
    RHS(t,population,param(4),param(5),param(6),param(7),param(8)...
    , param(9), param(10), param(11)),times , ic);
% Select only Infected population size
I = population(:,3);
% Compute error with respect to data
error = sum((I-num_tweets).^2);
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
