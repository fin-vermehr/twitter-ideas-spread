%data_2 = readcsv('~/data.csv');

function fit_curve()
data_1 = csvread('Trebes.csv');
% Susceptible populations sizes at t = 0
N = 15000000;
iS2 = 0;
iE = 0;
iI = 10;
iZ = 1;
iS1 = N -iS2 - iI -iZ;
ic = [iS1 iS2 iI iE iZ];
% Data used for fitting 
num_tweets = data_1(:, 1);
times = linspace(0, length(num_tweets) - 1, length(num_tweets));
% Initial values of the parameters to be fitted 

param0 = [200 0 50 0.5 0.5 0.5 2 1];
% param(1) - beta1
% param(2) - beta2
% param(3) - gamma
% param(4) - p
% param(5) - l
% param(6) - m
% param(7) - mu 
% param(8) - e
% Define lower and upper bound for the parameters
large = 10^7;
A = [];
B = [];
LB = [0 -1 0 0 0 0 0 0];
UB = [large large large 1 1 1 large large];
% Setting linear equalities
Aeq = [0 1 0 0 0 0 0 0];
beq = [0];
nonlcon = [];
% Declare options for fmincon
options = optimset('Display','iter','MaxFunEvals',Inf,'MaxIter',Inf,...
                       'PlotFcns',{@optimplotfval, @optimplotfunccount});
% Fit the parameters 
[param,E,exitflag] = fmincon(@(param) loss_function(param, times, num_tweets,...
    ic), param0, A, B, Aeq, beq,LB, UB, nonlcon, options);
[~, population] = ode23(@(t, population) ...
    RHS(t,population,param(1), param(2),param(3), param(4), param(5),param(6),param(7),param(8)),times , ic);
I = population(1:100,3);
S2 = population(1:100,2);
S1 = population(1:100,1);
Ex = population(1:100,4);
Z = population(1:100,5);
figure();
plot(times(1:100), [S1 S2 I Ex Z])
legend('Sus_1','Sus_2','E','I', 'Z')
figure()
plot(times, [population(:,3) num_tweets])
legend('Infected', 'Data')
xlabel('Time/(10min)')
ylabel('Number of Tweets')

for n = 1:8
fprintf('%4.10f\n', param(n))
end
display(E)
end

% Define loss function
function error = loss_function(param, times, num_tweets, ic)
% Solve ode, return population sizes with corresping times
[~, population] = ode23(@(t, population) ...
    RHS(t,population,param(1), param(2),param(3),param(4),param(5),param(6)...
    , param(7), param(8)),times , ic);
% Select only Infected population size
I = population(:,3);
% Compute error with respect to data
error = (norm(I-num_tweets)/norm(num_tweets));
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
