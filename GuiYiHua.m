% 文本特征矩阵归一化
clc,clear

load xunlian
load jianyan
load jisuan
load NotBass

[m,n] = size(NotBass);
NotBassGui = zeros(m,n);
for i = 1:m
   for j = 1:n
       NotBassGui(i,j) = NotBass(i,j) / sum(NotBass(i,1:end));
   end
end


[m,n] = size(xunlian);
xunlianGui = zeros(m,n);
for i = 1:m
   for j = 1:n
       xunlianGui(i,j) = xunlian(i,j) / sum(xunlian(i,1:end));
   end
end


[m,n] = size(x);
jisuanGui = zeros(m,n);
for i = 1:m
   for j = 1:n
       jisuanGui(i,j) = x(i,j) / sum(x(i,1:end));
   end
end


[m,n] = size(jianyan);
jianyanGui = zeros(m,n);
for i = 1:m
   for j = 1:n
       jianyanGui(i,j) = jianyan(i,j) / sum(jianyan(i,1:end));
   end
end
