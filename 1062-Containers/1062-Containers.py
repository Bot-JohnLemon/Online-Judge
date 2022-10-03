#   Online Judge Problem ID: 1062 result: Accepted
#   by JohnLemon069 :)

sample_input=input()
sample_input=list(sample_input)
times=0

def add_stack(i):
    cnt=0
    while cnt<len(containers):
            if sample_input[i]==containers[cnt]:
                return 0
            elif sample_input[i]<containers[cnt]:
                containers[cnt] = sample_input[i]
                return 0
            cnt=cnt+1
    if i == 0:
        containers[len(containers)-1] = sample_input[i]
    else:
        containers.append(sample_input[i])
    return 1

while sample_input != "end":
    sample_input=list(sample_input)
    containers=[]
    containers.append('\0')
    times=times+1
    i=0
    ans=0
    while i < len(sample_input):
        cnt=0
        ans=ans+add_stack(i)
        i=i+1
    print("Case " + str(times) + ": " + str(ans))
    sample_input=input()