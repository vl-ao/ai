import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data={
    'size':[1000,1500,2000,2500,3000],
    'bedroom':[1,2,3,4,5],
    'age':[2,4,6,8,10],
    'price':[100000,200000,300000,400000,500000]
}


df=pd.DataFrame(data)

x=df[['size','bedroom','age']]
y=df[['price']]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

model=LinearRegression()

model.fit(x_train,y_train)

# prediction=model.predict(x_test)

print(model.coef_)
print(model.intercept_)