# Manuskript RPM packaging

## Overview

RPM spec file used to provide an automated build on copr : https://copr.fedorainfracloud.org/coprs/notsag/manuskript

## Local build

### Prepare build env

Follow the steps [here](https://developer.fedoraproject.org/deployment/rpm/about.html)

### Build

```shell
# Download sources
spectool -g -R manuskript.spec
# Build the rpm
rpmbuild -ba manuskript.spec
```

## Install

```shell
sudo dnf copr enable notsag/manuskript
sudo dnf install manuskript
```

