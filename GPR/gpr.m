addpath(genpath(pwd))  %将当前文件夹下的所有文件夹都包括进调用函数的目录

%将当前文件夹下的所有文件夹都包括进调用函数的目录
%下载数据
load('train.mat');
%% 乱序生成训练集和测试集
b = train_data;%所有样本
rowrank = randperm(size(b,2));  % size获得b的列数，randperm打乱各列的顺序
randIndex= b(:,rowrank);          % 按照rowrank重新排列各列，注意rowrank的位置
train =randIndex(:,1:2300);
test = randIndex(:,2301:2500);
%% 获得输入输出
 p_train = train(1:2,:);%训练样本输入
 t_train = train(3,:);%训练样本输出
 p_test = test(1:2,:);%测试样本输入
 t_test = test(3,:);%测试样本输出
 %% 转置 （因为我的数据结构是每一列为一组，而gp函数要求每一行为一组，所以做了一下转置）
pn_train = p_train';
tn_train = t_train';
pn_test = p_test';
tn_test = t_test';
%% 超参数优化
meanfunc = @meanConst;%设定均值函数
covfunc = @covRQiso; %协方差函数（RQ）
likfunc = @likGauss; %以及似然函数
hyp = struct('mean', 3, 'cov', [1 0 0], 'lik', -1);%均值/cov/lik超参数列向量的hyp结构
iter_times=0;

hyp2 = minimize(hyp, @gp, -20, @infGaussLik, meanfunc, covfunc, likfunc,pn_train, tn_train);
%% 预测
% yfit是预测平均值，ys是预测方差
[yfit ys] = gp(hyp2, @infGaussLik, meanfunc, covfunc, likfunc,pn_train, tn_train, pn_test);
%% 画图
plot(1:length(tn_test),tn_test,'r-*',1:length(tn_test),yfit,'b:o')
grid on
legend('真实值','预测值')
xlabel('样本编号')
ylabel('GDOP')
title('高斯过程回归预测值与真实值对比')
plotResult(tn_test, yfit) %结果可视化
title('高斯过程回归误差')
%% 计算误差
    error=yfit-tn_test;
    [len,~]=size(tn_test);
    MAE1=sum(abs(error./tn_test))/len;
    MSE1=error'*error/len;
    RMSE1=MSE1^(1/2);
    R = corrcoef(tn_test,yfit);
    r = R(1,2);
    % [R2 rmse] = rsquare(tn_test,yfit);
    disp(['迭代次数：',iter_times])
    disp(['.....高斯过程回归误差计算................'])
    disp(['平均绝对误差MAE为:',num2str(MAE1)])
    disp(['均方误差为MSE:',num2str(MSE1)])
    disp(['均方根误差RMSE为:',num2str(RMSE1)])
    disp(['决定系数 R^2为:',num2str(r)])





 

