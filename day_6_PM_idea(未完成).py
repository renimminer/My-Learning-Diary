def pm_idea(a):
    p = len(a) - 1
    task_order = []
    for i in a[1:]:
        task_order.append(i[0])
    print(task_order)
    task_priority = [a[1][2]]
    # for i in a[2:]:
    #     if


if __name__ == "__main__":
    a = [[2, 2, 4],
         [1, 1, 3, 5],
         [2, 1, 4, 3],
         [3, 2, 4, 3],
         [4, 2, 4, 3]]
