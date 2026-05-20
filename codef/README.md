# codef

[code fragments management](https://chat.deepseek.com/a/chat/s/ceb117fd-ab10-4f88-9cb2-6c1cb1c46d34)

```sh
 $ codef session new "Session name"
   * creates session with uuid
   * puts "name: Session name" into <session dir>/session.yaml
 $ codef session rename "New name"
 $ codef session rm "session-id-part"
 $ codef session ls
 
 $ codef add 
   * in case of TERM_PROGRAM=zed
   * checks environment variables
   * makes new fragment from variables in <session dir>
   * puts line numbers into session.yaml for basename
 $ codef (md|markdown)
   * build markdown file
   * outputs it to stdout
```

## dependencies

* jq
* fzf
* $EDITOR variable
* var codef.base
