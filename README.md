Need a big table in your latex document and don't want to type it out?

Just create a csv file and tabularize it

  $ ./tabularize.py data.csv # generates data.tex

Then in your tex-main, use \input inside your table:
%%%%%TEX EXAMPLE%%%%%
\begin{table}
\centering
\caption{Some Data}\label{tab:data}

\input{data.tex}

\end{table}
%%%%%END EXAMPLE%%%%%
%% COMMENTS %%
By default, tabularize calculates the number of columns and fills in the correct number of centering commands into the "\begin{tabular}[ccc...]" command.
  tabularize is set to generate "longtable" by default rather than "tabular", so add to your preamble:
    \usepackage{longtable}
  The default delimiter is a comma, but can be changed in line 14 
    Do not use with fixed-width files!

This script was written for a latex class that uses \toprule and \bottomrule. If your document only has \hrule, consider modifying lines 25 and 43, or use "\def\toprule{\hrule}" and "\def\bottomrule{\hrule}"

If you use latexmk, it seems like -cc and -pvc will auto compile your main whenever tabularize is run.
