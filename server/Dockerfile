FROM python:3.7-alpine as base
FROM base as builder

WORKDIR /work
RUN mkdir /build

COPY setup.py .
COPY job_server/ job_server/
RUN pip install --no-warn-script-location --prefix=/work/build .

FROM base

COPY --from=builder /work/build /usr/local
ENV PORT=8000
CMD ["job_server"]