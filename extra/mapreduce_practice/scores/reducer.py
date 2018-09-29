import sys

last_user = None

for line in sys.stdin:
    user, rec_type, value = line.strip().split('\t')

    count = 0
    sum_all = 0
    fav_subj = None
    if last_user is None:
        last_user = user
        if rec_type == 'score':
            count += 1
            sum_all += int(value)
        else:
            fav_subj = value
    elif user == last_user:
        if rec_type == 'score':
            count +=1
            sum_all += int(value)
        else:
            fav_subj = value
    else:
        last_user = user
        sys.stdout.write("{0}\t{1}\n".format(fav_subj, float(sum_all) / count))
        if rec_type == 'score':
            count = 1
            sum_all = int(value)
        else:
            fav_subj = value


sys.stdout.write("{0}\t{1}\n".format(fav_subj, float(sum_all) / count))


