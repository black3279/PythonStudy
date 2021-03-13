
import mymodule

selected = mymodule.random_rsp()

print(selected)

print('가위?', mymodule.SCISSOR == selected )
print('바위?', mymodule.ROCK == selected )
print('보?', mymodule.PAPER == selected )