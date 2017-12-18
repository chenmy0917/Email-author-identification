%归一化之后的文本特征矩阵求期望
clc,clear
load xunlianGui
load jisuanGui
load jianyanGui
load NotBassGui

[m,n] = size(xunlianGui);
xunlianAve = zeros(1,n);
for j = 1:n
    xunlianAve(1,j) = mean(xunlianGui(1:end,j));
end

[m,n] = size(jisuanGui);
jisuanAve = zeros(1,n);
for j = 1:n
    jisuanAve(1,j) = mean(jisuanGui(1:end,j));
end

[m,n] = size(jianyanGui);
jianyanAve = zeros(1,n);
for j = 1:n
    jianyanAve(1,j) = mean(jianyanGui(1:end,j));
end

[m,n] = size(NotBassGui);
NotBassAve = zeros(1,n);
for j = 1:n
    NotBassAve(1,j) = mean(NotBassGui(1:end,j));
end