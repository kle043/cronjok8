FROM python:3.7-alpine as base
FROM base as builder

WORKDIR /work
RUN mkdir /build

COPY setup.py .
COPY job_server/ job_server/
RUN pip install --prefix=/work/build .

FROM base

COPY --from=builder /work/build /usr/local

CMD ["job_server"]