# if __name__=='__main__'
# python checks if:
# 1.Module can be run as a standalone program
# 2.Module can be imported and used by other modules
# the reason ppl,include this is because of this adv
# in short we check if module is run directly or indirectly
# Python interpreter sets special vars and one of which is __name__
# then python will execute the code found within __main__
# py will assign '__main__'val to '__name__' if its the initial module being run
# 1.without importing module

# print(__name__)

# 2.with importing a module
import module_two
print(__name__)
print(module_two.__name__)  # name is then assigned the module name
