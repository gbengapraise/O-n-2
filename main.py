def func(n):
    iteration = 0

    for i in range(0,n):
        for j in range(0,n):
            iteration += 1
            print('*', end='')
        print('\n')

    print(f'For input size {n}, the iteratiion: {iteration}')

func(5)
func(100)

