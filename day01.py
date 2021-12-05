def count_depth_increases(sonar_readings):
    increases = 0
    for i in range(1, len(sonar_readings)):
        if sonar_readings[i-1] < sonar_readings[i]:
            increases = increases + 1
    return increases


def windowed_depths(depths):
    window = []
    for i in range(2, len(depths)):
        window.append(depths[i-2] + depths[i-1] + depths[i])
    return window


def day01_part01(depths):
    return count_depth_increases(depths)


def day01_part02(depths):
    return count_depth_increases(windowed_depths(depths))