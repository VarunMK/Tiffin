#!/bin/sh
exec ${OPENVSCODE_SERVER_ROOT}/bin/openvscode-server --host 0.0.0.0 --without-connection-token "${@}" -- &
node /src/index.js