from .base import *

MIDDLEWARE_CLASSES += (
    #'cms.middleware.utils.ApphookReloadMiddleware',
    #'cms.middleware.user.CurrentUserMiddleware',
    #'cms.middleware.page.CurrentPageMiddleware',
    #'cms.middleware.toolbar.ToolbarMiddleware',
    #'cms.middleware.language.LanguageCookieMiddleware'
)

INSTALLED_APPS += (
    # 'cms',
    # 'menus',
    # 'sekizai',
    # 'treebeard',
    # 'djangocms_text_ckeditor',
    # 'filer',
    # 'easy_thumbnails',
    # 'cmsplugin_filer_image',
    # 'cmsplugin_filer_file',
    # 'cmsplugin_filer_folder',
    # 'cmsplugin_filer_teaser',
    # 'cmsplugin_filer_utils',
    # 'cmsplugin_filer_video',
)


# ==============================================================================
# Django-CMS
# ==============================================================================

CMS_LANGUAGES = {
    'default': {
        'public': True,
        'hide_untranslated': False,
        'redirect_on_fallback': True,
    },
    1: [
        {
            'public': True,
            'code': 'en',
            'hide_untranslated': False,
            'name': gettext('en'),
            'redirect_on_fallback': True,
        },
    ],
}

CMS_TEMPLATE_INHERITANCE = True

CMS_TEMPLATES_DIR = {
    1: os.path.join(PROJECT_DIR, 'templates/cms'),
}

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

detail_placeholder_conf = {
    'plugins': [
        'SliderStagePlugin',
        'TeaserSliderStagePlugin',
        'TileStagePlugin',
        'TextBlockPlugin',
        'ImageBlockPlugin',
    ],
}

CMS_PLACEHOLDER_CONF = {
    'hero_stage': {
        'plugins': [
            'MyPlugin'
        ]
    },
    'content': {
        'plugins': [
            'MyPlugin',
        ],
    },
    'teaser_row': {
        'plugins': [
            'MyPlugin',
        ],
    },
    'project_plugins': detail_placeholder_conf
}

# ==============================================================================
# Thumbnailing
# ==============================================================================

THUMBNAIL_PRESERVE_EXTENSIONS = ('png',)

THUMBNAIL_PROCESSORS = (
    #'easy_thumbnails.processors.colorspace',
    #'easy_thumbnails.processors.autocrop',
    #'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    #'easy_thumbnails.processors.filters'
)

# ==============================================================================
# Tagulous
# ==============================================================================

SERIALIZATION_MODULES = {
    'xml':    'tagulous.serializers.xml_serializer',
    'json':   'tagulous.serializers.json',
    'python': 'tagulous.serializers.python',
    'yaml':   'tagulous.serializers.pyyaml',
}
