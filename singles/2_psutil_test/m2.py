# source https://www.geeksforgeeks.org/how-to-get-current-cpu-and-ram-usage-in-python/

# 1
import psutil
N=2
print('The CPU usage is: ', psutil.cpu_percent(N)) # Calling psutil.cpu_precent() for N seconds


# # 2
# import psutil
# print(psutil.virtual_memory())
# # print(f'RAM memory used:{psutil.virtual_memory()[2]}%') # Getting % usage of virtual_memory (3rd field)
# # print(f'RAM Used {psutil.virtual_memory()[3]/1000000000}GB') # Getting usage of virtual_memory in GB (4th field)


# # 3
# import psutil
# N=1
# print('The CPU usage is: ', psutil.cpu_percent(N)) # Calling psutil.cpu_precent() for N seconds
# print(f'RAM memory used:{psutil.virtual_memory()[2]}%') # Getting % usage of virtual_memory (3rd field)
# print(f'RAM Used {psutil.virtual_memory()[3]/1000000000}GB') # Getting usage of virtual_memory in GB (4th field)
