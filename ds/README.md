# ds

deepseek cli

 $ ds auth
   : should import authentication 
   : from curl command line
   : imported from devtools
   : curl command line may be imported through clipboard

# when authorized
 $ ds session 
   : takes session url from cli
   : or from clipboard
   : and makes it current
 $ ds session list
   : lists last 100 sessions through api request
 $ ds session choose
   : lists sessions | fzf | makes session current

# when session is selected
 $ ds message
 $ ds message list
 $ ds message choose
 $ ds message files
