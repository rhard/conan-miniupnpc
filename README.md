[![Download](https://api.bintray.com/packages/rhard/conan/miniupnpc%3Arhard/images/download.svg)](https://bintray.com/rhard/conan/miniupnpc%3Arhard/_latestVersion)
[![Build Status](https://travis-ci.org/rhard/conan-miniupnpc.svg?branch=testing%2F2.1)](https://travis-ci.org/rhard/conan-miniupnpc)
[![Build status](https://ci.appveyor.com/api/projects/status/github/rhard/conan-miniupnpc?branch=testing%2F2.1&svg=true)](https://ci.appveyor.com/project/rhard/conan-miniupnpc)

[Conan.io](https://conan.io) package recipe for *miniupnpc*.

MiniUPnP client - an UPnP IGD control point

The packages generated with this **conanfile** can be found on [Bintray](https://bintray.com/rhard/public-conan/miniupnpc%3Arhard).

## For Users: Use this package

### Basic setup

    $ conan install miniupnpc/2.1@rhard/testing

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    miniupnpc/2.1@rhard/testing

    [generators]
    cmake

Complete the installation of requirements for your project running:

    $ mkdir build && cd build && conan install ..

Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they should not be added to the root of the project, nor committed to git.

## For Packagers: Publish this Package

The example below shows the commands used to publish to rhard conan repository. To publish to your own conan respository (for example, after forking this git repository), you will need to change the commands below accordingly.

## Build and package

The following command both runs all the steps of the conan file, and publishes the package to the local system cache.  This includes downloading dependencies from "build_requires" and "requires" , and then running the build() method.

    $ conan create . rhard/testing

### Available Options
| Option        | Default | Possible Values  |
| ------------- |:----------------- |:------------:|
| shared      | False |  [True, False] |

## Add Remote

    $ conan remote add rhard "https://api.bintray.com/conan/rhard/conan"

## Upload

    $ conan upload miniupnpc/2.1@rhard/testing --all -r rhard

## Conan Recipe License

NOTE: The conan recipe license applies only to the files of this recipe, which can be used to build and package miniupnpc.
It does *not* in any way apply or is related to the actual software being packaged.

[MIT](https://github.com/rhard/conan-miniupnpc.git/blob/master/LICENSE.md)
