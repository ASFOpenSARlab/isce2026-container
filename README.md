# isce2026-container

This repository publishes the OpenScienceLab container Docker image for the
deployment used in the Fall 2026 Earthscope Insar Processing and Analysis course.

This image is also runnable locally: all packages are publicly available
[here](https://github.com/orgs/ASFOpenSARlab/packages/container/package/isce2026-container).
Images available from this repo are tagged `v*.*.*`, `main`, or `sha-XXXXXX`. Long SHA tagged
"images" in the Package list are OCI artifacts that enable signiture verification (like with 
[`cosign verify`](https://github.com/sigstore/cosign#verify-a-container)), and will result in
an `unsupported media type application/vnd.oci.empty.v1+json` error if pulled locally.

To run the image used in the OpenScienceLab deployment environment, run
the following from the command line:

```bash
docker run -p 8888:8888 ghcr.io/asfopensarlab/isce2026-container:main
```

Click the `127.0.0.1:8888` link that appears, and you will be able to access the image.
