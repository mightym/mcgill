{{ project_name|lower }} CMS
========

Client-side code (CSS, JS, Static assets)
-----------------------------------------

Requires `npm` and `make`. Use `make help` for a list of targets.

The production assets will be built when running `npm install`. If it
is necessary to rebuild them, simply run

```
make
```

For development, install [watchman](https://facebook.github.io/watchman/docs/install.html)
and run:

```
npm install
make watch
```

To startup a Django runserver, browsersync, and file watching in parallel:

```
make run
```

To watch the styleguide and serve it with browsersync:

```
make run-styleguide
```
