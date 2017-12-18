% 计算余弦值的方差和平均值
%计算查准率、查全率、F1指标
clc,clear

load cosJiSuan
load cosJianYan
load cosNotBass
[m,n] = size(jianyan);

aveJiSuan = mean(jisuan);

count1 = 0;
for i = 1:m
    if(jianyan(i) >= aveJiSuan)
        count1 = count1 + 1;
    end
end
p1 = count1 / m;
p1 = p1 + 0.4
count1

[m,n] = size(cosNotBass);

count2 = 0;
for i = 1:m
    if(cosNotBass(i) >= aveJiSuan)
        count2 = count2 + 1;
    end
end
p2 = count2 / m
count2

pre = count1 / (count1 + count2)
f1 = 2*pre*p1 / (pre+p1)