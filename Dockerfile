FROM apache/airflow:2.5.0
COPY /dist /dagfs-dist
RUN cd /dagfs-dist && pip install $(ls -h | egrep '\.whl$' | tail -1)
