function sis()
data = csvread('GreatMills.csv');
num_tweets = data(:,1);
times = linspace(0, length(num_tweets) - 1, length(num_tweets));
param0 = [200 200];
iS = 60000000;
iI = 10;
ic = [iS iI]
% Parameters
% param(1) - beta
% param(2) - alpha
A = [];
B = [];
lb = zeros(2);
ub = [];
Aeq = [];
beq = [];
nonlcon = [];
% Declare options for fmincon
options = optimset('Display','iter','MaxFunEvals',Inf,'MaxIter',Inf,...
                       'PlotFcns',{@optimplotfval, @optimplotfunccount});
% Fit the parameters 
[param,E,exitflag] = fmincon(@(param) loss_function(param, times, num_tweets, ic), param0, A, B, Aeq, beq,lb, ub, nonlcon, options);
[~, population] = ode45(@(t, population) RHS(t, population, param(1), param(2)), times, ic);
I = population(:,2);
figure()
plot(times, [num_tweets, I])
legend('data', 'fit');
for n = 1:4
fprintf('%4.10f\n', param(n))
end
end
function error = loss_function(param, times, num_tweets, ic)
[~, population] = ode45(@(t, population) RHS(t, population, param(1), param(2)), times, ic);
I = population(:,2);
error = norm(I - num_tweets);
end
function dxdt = RHS(t, population, beta, alpha)
    S = population(1);
    I = population(2);
    dxdt = [-beta*S*I + alpha*I;
            beta*S*I - alpha*I;];
end