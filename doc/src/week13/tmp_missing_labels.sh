#rm -rf tmp_mako__* tmp_preprocess__*
find . -name '*.do.txt' -exec grep --color --with-filename --line-number "{eq:radialeqofmotion}" {} \;
find . -name '*.do.txt' -exec grep --color --with-filename --line-number "{eq:Ctrajectory}" {} \;
find . -name '*.do.txt' -exec grep --color --with-filename --line-number "{eq:Ctrajectory}" {} \;
