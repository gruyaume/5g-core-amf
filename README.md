# 5g-core-base

> **Warning**: This project is under construction!

Base project that other 5G core services can use to base themselves.

## Usage

Run <your service> using docker:

```bash
docker pull ghcr.io/gruyaume/5g-core-<your service>:main
docker run -p 8082:80 ghcr.io/gruyaume/5g-core-<your service>:main
```

## Reference

### API Framework

This project leverages [FastAPI](https://github.com/tiangolo/full-stack-fastapi-postgresql) web
  framework. 

### 5G Specification

This service has been created following the 
[ETSI specification for the <your service>](https://www.etsi.org/deliver/etsi_ts/129500_129599/129509/16.04.00_60/ts_129509v160400p.pdf).
Some common data models are also taken from this [specification sheet](https://www.etsi.org/deliver/etsi_ts/129500_129599/129571/15.03.00_60/ts_129571v150300p.pdf) from ETSI.
