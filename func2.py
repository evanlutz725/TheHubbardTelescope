#!/usr/bin/python3

def get_job_count_and_path(html):

    count_1 = 0
    count_2 = 0
    count_3 = 0

    for line in html:
        if 'jobsearch-JobCountAndSortPane-jobCount' in line:
            count_1 = 1
        if count_1:
            if '<span>' in line:
                count_2 = 1
        if count_2:
            if "jobs" in line:
                job_num = line.split()[0]
                count_1 = 0
                count_2 = 0
                count_3 = 1
        if count_3:
            if 'href' in line:
                objs = line.split()
                for obj in objs:
                    if 'href' in obj:
                        url_path = obj.split('"')[1]
                        return(job_num,url_path)


if __name__=="__main__":
    html = open('out.html')
    print(get_job_count(html))
