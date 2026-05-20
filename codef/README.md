# codef

code fragments management

```sh
 $ codef session new "Session name"
   * creates session with uuid
   * puts "name: Session name" into <session dir>/session.yaml
 $ codef add 
   * in case of TERM_PROGRAM=zed
   * checks environment variables
   * makes new fragment from variables in <session dir>
   * puts line numbers into session.yaml for basename
 $ codef (md|markdown)
   * build markdown file
   * outputs it to stdout
```
