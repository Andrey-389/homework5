immutable_var= tuple_ =2,4,6,8,False,'apple'
print(immutable_var)
print('tuple_[4]=True ошибка,так как элементы в кортеже неизменяемые')
mutable_list= list_=[1,3,5,7,9,True,'Wood']
print(mutable_list)
list_[0]=2,[1]*3
list_[5]=False
list_[6]='Tree'
print(mutable_list)