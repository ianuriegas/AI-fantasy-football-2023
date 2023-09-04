def starters_bench_creator(qbs, rbs, wrs, tes, kickers, defenses):
    for qb in qbs:
        player_names = (player_name for player_name, _ in qb)
        print(*player_names)

    for rb in rbs:
        player_names = (player_name for player_name, _ in rb)
        print(*player_names)

print("test")