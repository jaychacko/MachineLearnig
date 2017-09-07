# Data Preprocessing 

#import dataset
dataset = read.csv('Data.csv')

#missing value fix
#age
dataset$Age = ifelse(is.na(dataset$Age),ave(
  dataset$Age,FUN = function(x)mean(x,na.rm = TRUE)),
  dataset$Age)
#salary
dataset$Salary = ifelse(is.na(dataset$Salary),ave(
  dataset$Salary,FUN = function(x)mean(x,na.rm = TRUE)),
  dataset$Salary)

#encoding categorical data
dataset$Country = factor(dataset$Country,levels = c('France','Spain','Germany')
                         ,labels = c(1,2,3))
dataset$Purchased = factor(dataset$Purchased,levels = c('No','Yes')
                         ,labels = c(0,1))

#splitting test and training
#install.packages('caTools')

library(caTools)

set.seed(123)
split = sample.split(dataset$Purchased,SplitRatio = 0.8)
trainig_set  =subset(dataset,split ==TRUE)
test_set  =subset(dataset,split ==FALSE)


#featurscaling
#excluding 2 and 3 column since they are not numbers since we only foctored it 

trainig_set [,2:3]= scale(trainig_set[,2:3])
test_set[,2:3] = scale(test_set[,2:3])


















