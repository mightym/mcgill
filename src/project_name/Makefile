SHELL=/bin/bash -eu -o pipefail
NPM_BIN := $(shell pwd)/node_modules/.bin

# Only used in debug builds
PROJECT_NAME := $(shell pwd | rev | cut -d'/' -f1 | rev)
NOTIFY_CMD = $(NPM_BIN)/notify -t "Error" -m "The ${PROJECT_NAME} build broke!" -s Funk

#     ___                   __
#    /   |  _____________  / /______
#   / /| | / ___/ ___/ _ \/ __/ ___/
#  / ___ |(__  |__  )  __/ /_(__  )
# /_/  |_/____/____/\___/\__/____/


ASSETS_PATH = client/assets

assets:   ## Collect assets
	# Just copy them. No processing necessary
	mkdir -p build
	rsync -av --delete ${ASSETS_PATH}/ build/assets


#    ______    ________
#   / ___/ |  / / ____/
#   \__ \| | / / / __
#  ___/ /| |/ / /_/ /
# /____/ |___/\____/


SVG_PATH = client/svg

build/svg:
	mkdir -p $@

build/svg/%.svg: build/svg ${SVG_PATH}/%.svg
	$(NPM_BIN)/svgo --input ${SVG_PATH}/$*.svg --output $@

# convert `client/svg/*.svg` to `build/svg/*.svg`
svg: $(patsubst ${SVG_PATH}/%.svg,build/svg/%.svg,$(wildcard ${SVG_PATH}/*.svg))    ## Compress SVG files


#    ________________
#   / ____/ ___/ ___/
#  / /    \__ \\__ \
# / /___ ___/ /__/ /
# \____//____/____/


# Directory containing SCSS source files
SCSS_PATH = client/scss

# List of all SCSS files (recursive)
SCSS_FILES := $(shell find ${SCSS_PATH} -name "*.scss")

# List of all SCSS files, excluding those that begin with an underscore
SCSS_ROOTS := $(shell find ${SCSS_PATH} ! -name "_*.scss" -name "*.scss")

SASS_CMD = $(NPM_BIN)/node-sass --include-path ${SCSS_PATH}
SASS_DEBUG_OPTS = --source-map=true --source-map-contents=true --source-map-embed=true
SASS_PROD_OPTS = --output-style compressed
AUTOPREFIXER = $(NPM_BIN)/postcss --use autoprefixer --autoprefixer.browsers "last 2 versions"


build/css:
	# Make build directory
	mkdir -p $@

# Toggle between production and debug builds using DEBUG=1
buildcss = $(SASS_CMD) $(SASS_PROD_OPTS) $(1) | $(AUTOPREFIXER) > $(2)
ifdef DEBUG
buildcss = $(SASS_CMD) $(SASS_DEBUG_OPTS) $(1) > $(2) || $(NOTIFY_CMD)
endif

build/css/%.css: ${SCSS_FILES} build/css
	$(call buildcss,${SCSS_PATH}/$*.scss,$@)


# Only create CSS for root SCSS files
# convert `client/scss/*.scss` to `build/css/*.css`
css: $(patsubst ${SCSS_PATH}/%.scss,build/css/%.css,${SCSS_ROOTS})    ## Build CSS targets

#        __                  _____           _       __
#       / /___ __   ______ _/ ___/__________(_)___  / /_
#  __  / / __ `/ | / / __ `/\__ \/ ___/ ___/ / __ \/ __/
# / /_/ / /_/ /| |/ / /_/ /___/ / /__/ /  / / /_/ / /_
# \____/\__,_/ |___/\__,_//____/\___/_/  /_/ .___/\__/
#                                         /_/

# Directory containing JS source files
JS_PATH = client/js

# List of all JS files (recursive)
JS_FILES := $(shell find ${JS_PATH} -name "*.js")

build/js:
	mkdir -p $@

# Toggle between production and debug builds using DEBUG=1
# js -> browserify -> uglify
buildjs = $(NPM_BIN)/browserify $(1) | $(NPM_BIN)/uglifyjs -m -c warnings=false > $(2)
ifdef DEBUG
buildjs = $(NPM_BIN)/browserify --debug $(1) > $(2) || $(NOTIFY_CMD)
endif

build/js/%.bundle.js: ${JS_FILES} build/js
	$(call buildjs,${JS_PATH}/$*.js,$@)

# Only create bundles for top-level JS files
# convert `client/js/*.js` into `build/js/*.bundle.js`
js: $(patsubst ${JS_PATH}/%.js,build/js/%.bundle.js,$(wildcard ${JS_PATH}/*.js))    ## Build JavaScript targets


#     ____                                        __        __  _
#    / __ \____  _______  ______ ___  ___  ____  / /_____ _/ /_(_)___  ____
#   / / / / __ \/ ___/ / / / __ `__ \/ _ \/ __ \/ __/ __ `/ __/ / __ \/ __ \
#  / /_/ / /_/ / /__/ /_/ / / / / / /  __/ / / / /_/ /_/ / /_/ / /_/ / / / /
# /_____/\____/\___/\__,_/_/ /_/ /_/\___/_/ /_/\__/\__,_/\__/_/\____/_/ /_/
#


KSS_CSS = build/docs/styleguide/public/kss.css

${KSS_CSS}: build-styleguide
	$(NPM_BIN)/node-sass $(KSS_CSS:.css=.scss) $@

build/docs/styleguide/static:
	mkdir -p build/docs/styleguide
	#ln -s ../.. build/docs/styleguide/static

build-styleguide: build/docs/styleguide/static all
	$(NPM_BIN)/kss-node --config client/kss-config.json --custom chromeless --custom full

styleguide: ${KSS_CSS}    ## Build the styleguide


#     __  ____
#    /  |/  (_)_________
#   / /|_/ / / ___/ ___/
#  / /  / / (__  ) /__
# /_/  /_/_/____/\___/


clean:    ## Empty build directory
	rm -rf build/*

all: assets svg css js   ## Build all targets

.PHONY: all clean css js assets svg build-styleguide styleguide watch watch-styleguide runserver browsersync bs-styleguide run run-styleguide jslint pylint sasslint heroku help
.DEFAULT_GOAL := all

#     ____                 __                                 __
#    / __ \___ _   _____  / /___  ____  ____ ___  ___  ____  / /_
#   / / / / _ \ | / / _ \/ / __ \/ __ \/ __ `__ \/ _ \/ __ \/ __/
#  / /_/ /  __/ |/ /  __/ / /_/ / /_/ / / / / / /  __/ / / / /_
# /_____/\___/|___/\___/_/\____/ .___/_/ /_/ /_/\___/_/ /_/\__/
#                             /_/


# These aren't real `make` targets, but are useful helpers in development

watch:    ## Watch JS, CSS, and Assets for changes
	$(MAKE) DEBUG=1 all
	watchman-make -p '${JS_PATH}/**/*.js' -t DEBUG=1 js \
				  -p '${SCSS_PATH}/**/*.scss' -t DEBUG=1 css \
				  -p '${ASSETS_PATH}/**' -t assets \
				  -p '${SVG_PATH}/**' -t DEBUG=1 svg

watch-styleguide:    ## Watch for changes to styleguide
	$(MAKE) DEBUG=1 styleguide
	watchman-make -p '${SCSS_PATH}/**/*.scss' '${SCSS_PATH}/**/*.hbs' -t DEBUG=1 styleguide

runserver:    ## Django runserver
	DJANGO_SETTINGS_MODULE=nols_cms.settings.dev ./nols_website/manage.py runserver

browsersync:    ## Run browsersync as a proxy to runserver
	$(NPM_BIN)/browser-sync start --proxy="localhost:8000" --files="build/css"

bs-styleguide: styleguide    ## Run browsersync on styleguide
	$(NPM_BIN)/browser-sync start --config=client/bs-config.js

run:    ## Run `watch`, `runserver`, and `browsersync` in parallel
	$(MAKE) -j3 watch runserver browsersync


run-styleguide:    ## Run `watch-styleguide` and `bs-styleguide` in parallel
	$(MAKE) -j2 watch-styleguide bs-styleguide

jslint:   ## Lint JavaScript files
	$(NPM_BIN)/eslint ${JS_PATH}

sasslint:   ## Lint SCSS files
	$(NPM_BIN)/sass-lint ${SCSS_FILES} --verbose --no-exit --config client/.sass-lint.yml

pylint:    ## Lint Python files
	flake8 nols --statistics --exclude="*/migrations/*"

heroku:    ## Deploy current branch to Heroku
	heroku config:set RELEASE_VERSION=`git describe --abbrev=4`
	git push heroku `git rev-parse --abbrev-ref HEAD`:master

help:
	@echo -e "$$(grep -hE '^\S+:.*##' $(MAKEFILE_LIST) | sed -e 's/:.*##\s*/:/' -e 's/^\(.\+\):\(.*\)/\\x1b[36m\1\\x1b[m:\2/' | column -c2 -t -s :)"
