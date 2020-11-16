FROM python:3.7-alpine as base
FROM base as builder

WORKDIR /work
RUN mkdir /build

COPY setup.py .
COPY worker/ worker/
RUN pip install --no-warn-script-location --prefix=/work/build .

FROM base

COPY --from=builder /work/build /usr/local

ENTRYPOINT ["worker"]
CMD ["--help"]