from distutils.core import setup
setup(
  name = 'jspaste.py',         
  packages = ['jspaste.py'],   
  version = '0.1',      
  license='MIT',        
  description = 'Api Wrapper Of Jspaste, https://jspaste.tnfangel.repl.co/',   
  author = 'Pruebando',                   
 
  url = 'https://github.com/pruebando/jspaste',   
  download_url = 'https://github.com/pruebando/jspaste/archive/refs/tags/0.1.tar.gz',   
  keywords = ['Pastebin', 'Jspaste', 'Api Wrapper'],   
  install_requires=[           
          'requests'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',    
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License ::  MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
