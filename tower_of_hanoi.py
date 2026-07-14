def tower_of_hanoi(n,source,auxillary,destination):
  if n == 1:
    print(f"move disk 1 from {source} --> {destination}")
    return
  
  tower_of_hanoi(n-1,source,destination,auxillary)
  print(f"move disk {n} from {source} --> {destination}")

  tower_of_hanoi(n-1,auxillary,destination,source)
n=int(input("Enter number of disks"))
tower_of_hanoi(n,'A','C','B')