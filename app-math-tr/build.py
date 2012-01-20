import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    cmd = "pdftk */cover.pdf */model.pdf */karesel.pdf */invtrig.pdf \
pfractions/pfractions.pdf ratio/ratio.pdf poldiv/poldiv.pdf */fundamental.pdf  \
*/cauchy.pdf */integral-mult.pdf */lhosp*.pdf */euler.pdf intexp/intexp.pdf */taylor.pdf  \
*/taylor2d.pdf eig/eig.pdf */logaritma.pdf */complexity.pdf */probsolve.pdf \
 */id3.pdf */turev.pdf */totaldiff.pdf */eigseg.pdf */rayleigh.pdf \
exp/exp.pdf */moment.pdf */dagilimlar.pdf */buyuk.pdf */cebisev.pdf \
*/ml-tr.pdf */naive.pdf */mcmc.pdf */coal.pdf */simplex.pdf */qp.pdf \
*/svm.pdf */fem.pdf */fourier.pdf pde-wave-deriv/pde_01.pdf \
*/heat-deriv.pdf */heat.pdf */curvature.pdf \
*/level.pdf */lk.pdf */varcalc.pdf */filter.pdf */phd.pdf \
output ~/Dropbox/Public/skfiles/app-math-tr.pdf "
    os.system(cmd)
    exit()
