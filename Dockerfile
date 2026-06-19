FROM ghcr.io/asfopensarlab/deployment-opensarlab-container_sar:v1.3.2

ARG PIXI_MANIFEST_PATH=/tmp/pixi.toml

## Build Pixi environment

COPY pixi.toml ${PIXI_MANIFEST_PATH}

RUN pixi install --manifest-path ${PIXI_MANIFEST_PATH}

## Register Pixi environment with ipykernel

RUN pixi run --manifest-path ${PIXI_MANIFEST_PATH} -e default python -m ipykernel install --user --name default --display-name earthscope_insar

## Make Bash in jupyter notebook run using pixi

COPY setup_notebook_shell.py /tmp/setup_notebook_shell.py

RUN python /tmp/setup_notebook_shell.py --manifest-path ${PIXI_MANIFEST_PATH}
