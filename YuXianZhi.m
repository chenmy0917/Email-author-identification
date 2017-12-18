% 计算每封邮件和模板之间的cos
clc,clear
load jiSuanMoBan
load jianYanMoBan
load ontBassMoBan


[m,n] = size(jiSuanMoBan);
cosJiSuan = zeros(m,1);

for i = 2:m
    count = 0;    
    count1 = 0;    
    count2 = 0;
    for j = 1:n
        if(jiSuanMoBan(i,j) ~= 0)
            count = count + jiSuanMoBan(1,j) * jiSuanMoBan(i,j);
            count1 = count1 + jiSuanMoBan(1,j) * jiSuanMoBan(1,j);
            count2 = count2 + jiSuanMoBan(i,j) * jiSuanMoBan(i,j);
        end
    end
    cosJiSuan(i) = count / (sqrt(count1) * sqrt(count2));
end

[m,n] = size(jianYanMoBan);
cosJianYan = zeros(m,1);

for i = 2:m
    count = 0;    
    count1 = 0;    
    count2 = 0;
    for j = 1:n
        if(jianYanMoBan(i,j) ~= 0)
            count = count + jianYanMoBan(1,j) * jianYanMoBan(i,j);
            count1 = count1 + jianYanMoBan(1,j) * jianYanMoBan(1,j);
            count2 = count2 + jianYanMoBan(i,j) * jianYanMoBan(i,j);
        end
    end
    cosJianYan(i) = count / (sqrt(count1) * sqrt(count2));
end


[m,n] = size(notBass);
cosNotBass = zeros(m,1);
for i = 2:m
    count = 0;    
    count1 = 0;    
    count2 = 0;
    for j = 1:n
        if(notBass(i,j) ~= 0)
            count = count + notBass(1,j) * notBass(i,j);
            count1 = count1 + notBass(1,j) * notBass(1,j);
            count2 = count2 + notBass(i,j) * notBass(i,j);
        end
    end
    cosNotBass(i) = count / (sqrt(count1) * sqrt(count2));
end