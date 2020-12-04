import pylint.lint
pylint_opts = ['main.py', 'weather_update.py', 'news_filter.py', 'covid_update.py'] 
pylint.lint.Run(pylint_opts)
