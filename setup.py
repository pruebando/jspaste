from distutils.core import setup
setup(
  name = 'jspaste.py',         # How you named your package folder (MyLib)
  packages = ['jspaste.py'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Api Wrapper Of Jspaste, https://jspaste.tnfangel.repl.co/',   # Give a short description about your library
  author = 'YOUR NAME',                   # Type in your name
 
  url = 'https://github.com/pruebando/jspaste',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/pruebando/jspaste/archive/refs/tags/0.1.tar.gz',    # I explain this later on
  keywords = ['Pastebin', 'Jspaste', 'Api Wrapper'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'requests'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License ::  MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
