mkdir package
cd mac_build

function generate_app() {
    python setup_"$1".py py2app -A

    mv "dist/$1.app" "../package/$1.app"
    rm -rf build
    rm -rf dist
}

generate_app message
generate_app connect
