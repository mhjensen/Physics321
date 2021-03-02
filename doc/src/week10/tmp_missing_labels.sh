#rm -rf tmp_mako__* tmp_preprocess__*
find . -name '*.do.txt' -exec grep --color --with-filename --line-number "{eq:fastdriven1}" {} \;
find . -name '*.do.txt' -exec grep --color --with-filename --line-number "{eq:fastdriven2}" {} \;
find . -name '*.do.txt' -exec grep --color --with-filename --line-number "{eq:partform}" {} \;
find . -name '*.do.txt' -exec grep --color --with-filename --line-number "{eq:Ddrive}" {} \;
find . -name '*.do.txt' -exec grep --color --with-filename --line-number "{eq:homogsolution}" {} \;
