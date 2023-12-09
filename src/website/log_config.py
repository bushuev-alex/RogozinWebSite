LOGGING = {'version': 1,
           'disable_existing_loggers': False,
           'style': '{',
           'formatters': {'all': {'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'},
                          'info': {'format': '%(asctime)s %(levelname)s %(module)s %(message)s'},
                          'security': {'format': '%(asctime)s %(levelname)s %(module)s %(message)s'},
                          'debug': {'format': '%(asctime)s %(levelname)s %(message)s'},
                          'warning': {'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s'},
                          'error': {'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s %(exc_info)s'},
                          'mail': {'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s'},
                          'critical': {'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s %(exc_info)s'}
                          },
           'filters': {'require_debug_true': {'()': 'django.utils.log.RequireDebugTrue'},
                       'require_debug_false': {'()': 'django.utils.log.RequireDebugFalse'},
                       },
           'handlers': {'INFO_file': {'level': 'INFO',
                                      'filters': ['require_debug_false'],
                                      'class': 'logging.FileHandler',
                                      'filename': 'general.log',
                                      'formatter': 'info'
                                      },
                        'DEBUG': {'level': 'DEBUG',
                                  'filters': ['require_debug_true'],
                                  'class': 'logging.StreamHandler',
                                  'formatter': 'debug'
                                  },
                        'WARNING': {'level': 'WARNING',
                                    'filters': ['require_debug_true'],
                                    'class': 'logging.StreamHandler',
                                    'formatter': 'warning'
                                    },
                        'ERROR': {'level': 'ERROR',
                                  'filters': ['require_debug_true'],
                                  'class': 'logging.StreamHandler',
                                  'formatter': 'error'
                                  },
                        'ERROR_file': {'level': 'ERROR',
                                       'filters': ['require_debug_true'],
                                       'class': 'logging.FileHandler',
                                       'filename': 'error.log',
                                       'formatter': 'error'
                                       },
                        'CRITICAL': {'level': 'CRITICAL',
                                     'filters': ['require_debug_true'],
                                     'class': 'logging.StreamHandler',
                                     'formatter': 'critical'
                                     },
                        'CRITICAL_file': {'level': 'CRITICAL',
                                          'filters': ['require_debug_true'],
                                          'class': 'logging.FileHandler',
                                          'filename': 'error.log',
                                          'formatter': 'critical'
                                          },
                        'mail_admins': {'level': 'ERROR',
                                        'filters': ['require_debug_false'],
                                        'class': 'django.utils.log.AdminEmailHandler',
                                        'formatter': 'mail'
                                        },
                        'SEC_file': {'level': 'INFO',
                                     'filters': ['require_debug_true'],
                                     'class': 'logging.FileHandler',
                                     'filename': 'security.log',
                                     'formatter': 'security'
                                     },
                        },
           'loggers': {'django': {'handlers': ['INFO_file', 'DEBUG', 'ERROR', 'CRITICAL', 'WARNING'],
                                  'propagate': True,
                                  },
                       'django.request': {'handlers': ['mail_admins', 'ERROR_file', 'CRITICAL_file'],
                                          'level': 'ERROR',
                                          'propagate': False,
                                          },
                       'django.server': {'handlers': ['mail_admins', 'ERROR_file', 'CRITICAL_file']},
                       'django.template': {'handlers': ['ERROR_file', 'CRITICAL_file']},
                       'django.db.backends': {'handlers': ['ERROR_file', 'CRITICAL_file']},
                       'django.security': {'handlers': ['SEC_file']}
                       }
           }