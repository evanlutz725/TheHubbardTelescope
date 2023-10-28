#!/usr/bin/python3

def get_job_count(html):

    count_1 = 0
    count_2 = 0

    for line in html:
        if 'jobsearch-JobCountAndSortPane-jobCount' in line:
            count_1 = 1
        if count_1:
            if '<span>' in line:
                count_2 = 1
        if count_2:
            if "jobs" in line:
                job_num = line.split()[0]
                break

    return(job_num)

if __name__=="__main__":
    html = open('out.html')
    print(get_job_count(html))
