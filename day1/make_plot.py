import matplotlib.pyplot as plt


# same files, change workers

workers = [1, 2, 4, 6, 8, 10]
time_taken = [3.545, 2.294, 1.655, 1.459, 1.377, 1.386, ]
plt.plot(workers, time_taken)
plt.xlabel("workers")
plt.ylabel("time taken")
  
# saving the file.Make sure you 
# use savefig() before show().
plt.savefig("fig1.png")
plt.show()
# same workers, change files processes

files = [10, 20, 30, 40, 50, 60]
time_taken = [0.573, 0.669, 0.895, 1.062, 1.309, 1.565]
plt.plot(files, time_taken)
plt.xlabel("files")
plt.ylabel("time taken")
  
# saving the file.Make sure you 
# use savefig() before show().
plt.savefig("fig2.png")
plt.show()

