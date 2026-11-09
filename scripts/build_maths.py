from pathlib import Path
import json, math
ROOT=Path(__file__).resolve().parents[1]
lessons=[]
# Original prose and assessment tasks; IDs are local lesson IDs, not IB outcome codes.
def L(id,title,hl,tool,formula,concept,method,worked,steps,answer,practice,value,unit,mc,options,correct,why):
 topic=id.split('.')[0]
 lessons.append(dict(id=id,topic=topic,title=title,hl=hl,tool=tool,formula=formula,
 explanation=concept.split('|'),method=method.split('|'),worked=dict(question=worked,steps=steps.split('|'),answer=answer),
 practice=dict(question=practice,value=value,unit=unit),mc=dict(question=mc,options=options.split('|'),correct=correct,why=why)))
L('A1.1','Function notation, domain and range',False,'graph','y = f(x)',
 'A function assigns exactly one output to each permitted input. The notation f(3) asks for the output when the input is 3; it is not the product of f and 3.|The domain describes allowed inputs; the range describes resulting outputs. In a height model, time may be restricted to the interval before an object hits the ground even if the formula accepts all real inputs.|A graph can represent a function only if a vertical line cannot cross it twice. Different inputs may still give the same output. Always attach units to the input and output when interpreting a model.',
 'Identify the input and output variables.|Substitute with brackets around negative inputs.|Find restrictions from context, denominators or square roots.|Use a graph and endpoints to determine the range.',
 'For f(x)=x²+1 on −2 ≤ x ≤ 3, find the range.',
 'The lowest output occurs at x=0, which belongs to the domain.|f(0)=1; at the endpoints f(−2)=5 and f(3)=10.|The range is all values from 1 to 10, including both ends.','1 ≤ f(x) ≤ 10',
 'Let g(x)=3x²−2. Calculate g(−2).',10,'',
 'Which set describes the domain of a function?','Allowed inputs|Resulting outputs|Only the turning points|Only positive values',0,'The domain is the set of inputs for which the function is defined.')
L('A1.2','Reading graphs and solving intersections',False,'intersection','f(x) = g(x)',
 'An intersection solves two equations simultaneously: at that input both graphs have the same output. A root is the special case where one graph is y=0.|A calculator finds numerical coordinates inside a chosen window. A missing intersection can be outside that window; changing the display does not change the function.|Write the equation you solved and give only solutions inside the real-world domain. An x-coordinate alone is a solution of f(x)=g(x), while a coordinate pair describes an intersection.',
 'Enter both functions.|Set a window that includes their relevant behavior.|Find each intersection with the graph-analysis tool.|Check by substitution and reject inappropriate domain values.',
 'Find the intersections of y=x² and y=2x+3.',
 'Set x²=2x+3, or x²−2x−3=0.|Factor to (x−3)(x+1)=0, giving x=−1 and x=3.|Substitute to obtain the intersection coordinates.','(−1,1) and (3,9)',
 'The graphs y=2x+1 and y=7 meet. What is the x-coordinate?',3,'',
 'What does the x-coordinate of an intersection solve?','f(x)=g(x)|f(x)=0 in every case|f′(x)=0 in every case|The maximum of f',0,'At the intersection both function values are equal.')
L('A2.1','Linear models and interpreting parameters',False,'graph','y = mx + c',
 'A linear model assumes equal changes in input produce equal changes in output. Its gradient is the rate of change, with units of output per input unit.|The intercept is the predicted output at x=0. This may be meaningful, such as a fixed fee, or outside the range where the model was fitted.|Two distinct points determine a line exactly. A line fitted to many measurements usually leaves residuals because real observations vary.',
 'Compute change in y divided by change in x.|Use either point to find the intercept.|State the equation with named variables.|Interpret both parameters and the appropriate interval.',
 'A taxi costs €9 for 2 km and €21 for 8 km. Find a linear fare model.',
 'Gradient=(21−9)/(8−2)=2 euros per kilometre.|Use 9=2×2+c to obtain c=5.|The fixed fee is €5 and the distance charge is €2 per km.','C=2d+5',
 'For C=3d+4, calculate the cost of a 6 km trip.',22,'euros',
 'In a taxi model C=2d+5, what does 5 represent?','Fixed starting charge|Charge per kilometre|Maximum distance|Total distance',0,'At zero distance the model charges 5; this is the fixed fee.')
L('A2.2','Quadratic models, roots and vertices',False,'minimum','y = a(x−h)² + k',
 'A quadratic graph has one turning point. In vertex form (h,k) is visible directly; the sign of a determines whether it is a minimum or maximum.|Roots are input values where the output is zero. They may model the start and end of a flight, but only those in the physical domain are relevant.|Expanded, factorised and vertex forms emphasize different features. A calculator can help identify a vertex, but a sketch still needs labelled axes, key points and a sensible scale.',
 'Identify the opening direction and axis of symmetry.|Read or calculate the vertex.|Find roots with algebra or graph analysis.|Restrict the model to the real situation.',
 'For h(t)=−5(t−2)²+20, find the maximum height and its time.',
 'The negative coefficient makes the parabola open downward.|The vertex is (2,20).|Therefore the greatest height is 20 metres at 2 seconds.','20 m at t=2 s',
 'For f(x)=2(x−3)²+7, what is the minimum value?',7,'',
 'If a<0 in y=a(x−h)²+k, the vertex is a…','Maximum|Minimum|Vertical asymptote|Root in every case',0,'The graph opens downward, so its vertex is the highest point.')
L('A2.3','Fitting polynomial and cubic models',False,'regression','y = ax³ + bx² + cx + d',
 'A polynomial combines non-negative integer powers of the input. A cubic can model a change in curvature and may have two turning points, unlike a quadratic.|More parameters allow a model to fit more features, but they can also fit noise. A perfect fit to a few data points does not prove predictive reliability.|Choose the model using context, graph shape and residuals. Extrapolating a high-degree polynomial beyond the observed interval can give unrealistic results very quickly.',
 'Plot paired measurements.|Choose a plausible degree from the context and graph.|Fit the model and store the coefficients without early rounding.|Check residuals and restrict prediction to a justified interval.',
 'A model is f(x)=x³−3x+2. Find the prediction at x=2.',
 'Substitute 2 into every occurrence of x.|Evaluate 8−6+2.|The predicted output is 4; its units depend on the context.','f(2)=4',
 'For p(x)=2x³−x+1, calculate p(2).',15,'',
 'Why might a higher-degree polynomial be a poor choice?','It can fit noise and extrapolate badly|It always has fewer parameters|It cannot have turning points|It always predicts negative outputs',0,'Extra flexibility may overfit rather than explain the underlying relationship.')
L('A3.1','Inverse variation and asymptotes',False,'graph','y = k/x, x ≠ 0',
 'In inverse proportion, doubling one variable halves the other. The product xy stays constant, unlike direct proportion where y/x stays constant.|The reciprocal graph approaches the axes without crossing them when k is nonzero. An asymptote describes limiting behavior, not a physical barrier in every possible function.|The formula is undefined at x=0. In contexts such as sharing a fixed job between workers, only positive inputs may make sense.',
 'Check whether products xy are constant.|Find k from one observation.|Write y=k/x with its domain.|Interpret changes multiplicatively.',
 'Six workers take 10 hours for a fixed task. Predict the time for 15 equally productive workers.',
 'Total work is 6×10=60 worker-hours.|Use t=60/n.|At n=15, t=60/15=4 hours.','4 hours',
 'If y=48/x, find y when x=8.',6,'',
 'For inverse proportion y=k/x, which expression stays constant?','xy|x+y|y/x|x−y',0,'Multiplying both sides by x gives xy=k.')
L('A3.2','Exponential growth and decay',False,'graph','P(t) = P₀ bᵗ',
 'Exponential change multiplies the output by a fixed factor in each equal time interval. A factor above 1 represents growth and a factor between 0 and 1 represents decay.|An exponential model assumes a fixed proportional rate. Context determines whether unlimited growth remains plausible over a long interval.|Identify the initial value at t=0 and use the time unit associated with the growth factor. A monthly percentage cannot be applied once per year without conversion.',
 'Convert a percentage to a multiplier.|Write the initial amount and time unit.|Calculate without intermediate rounding.|Check whether limiting resources make the prediction plausible.',
 'A population starts at 200 and grows by 5% annually. Predict it after 3 years.',
 'Use multiplier 1.05.|Compute 200×1.05³=231.525.|A whole-population prediction is approximately 232 individuals.','About 232',
 'An amount 500 decreases by 10% each year. Find the model value after 2 years.',405,'',
 'What characterizes exponential growth?','A fixed multiplier over equal intervals|A constant absolute increase|A fixed upper limiting value in every exponential model|A negative initial value',0,'Equal time steps multiply the value by the same factor.')
L('A4.1','Trigonometric functions and periodic models',False,'trig','y = a sin(bx+c)+d; period = 2π/|b| in radians',
 'A periodic model repeats after a fixed interval. Amplitude is the distance from the midline to a peak, while the vertical shift is the midline value.|The period depends on both b and angle units. In degrees it is 360/|b|; in radians it is 2π/|b|. Never mix the two settings.|A seasonal model is an approximation. Its fitted phase shift places the peaks correctly, and its domain should describe the period where the cycle is stable.',
 'Find maximum and minimum to obtain amplitude and midline.|Identify the period.|Check degree or radian mode.|Use a known peak or intercept to fit the phase.',
 'A tide ranges from 2 m to 8 m. Find its amplitude and midline.',
 'Amplitude=(8−2)/2=3 m.|Midline=(8+2)/2=5 m.|The height oscillates 3 m above and below 5 m.','Amplitude 3 m; midline 5 m',
 'A periodic quantity has maximum 17 and minimum 5. Find its amplitude.',6,'',
 'A sine curve has amplitude 4. What is its full peak-to-trough distance?','8|4|2|16',0,'The full vertical range is twice the amplitude.')
L('A5.1','Piecewise functions and model boundaries',False,'graph','f(x) = different rules on specified intervals',
 'A piecewise function applies different formulas to different parts of its domain. This is useful for tariffs, tax bands and staged behavior.|At each boundary decide which interval includes equality. Overlapping incompatible rules or missing boundary points make a definition ambiguous.|Continuity means the neighboring outputs meet at a boundary. A real tariff can have a jump, so continuity must be checked rather than assumed.',
 'Identify the interval containing the input.|Apply only that interval’s rule.|Check endpoints and equality signs.|Interpret any jump in the original context.',
 'A delivery fee is €4 for d≤5 km and 4+2(d−5) for d>5. Find the fee at 8 km.',
 'Eight exceeds 5, so use the second rule.|Extra distance is 8−5=3 km.|Fee=4+2×3=10 euros.','€10',
 'A fee is €4 for d≤5 km and 4+2(d−5) for d>5 km. Find the fee for 7 km.',8,'euros',
 'Why do interval endpoints matter in a piecewise model?','They decide which rule applies at a boundary|They always make the function discontinuous|They change every gradient|They remove the need for a domain',0,'The equality sign specifies the boundary value’s applicable formula.')
L('A6.1','Transformations of graphs',True,'graph','y = a f(b(x−h)) + k',
 'Outside changes affect outputs: adding k shifts vertically and multiplying by a scales vertically. Inside changes affect inputs and often have the opposite-looking direction.|For y=f(x−h), a point moves right by h. For y=f(bx), horizontal distances scale by 1/|b|. Negative multipliers introduce reflections.|Track known points rather than memorising isolated phrases. Operations do not always commute; a shift followed by a stretch may differ from a stretch followed by a shift.',
 'Choose identifiable points on the original graph.|Map the input coordinate and then the output coordinate.|Rebuild the transformed graph.|Check asymptotes and the domain.',
 'The point (2,3) lies on y=f(x). Find its image on y=2f(x−4)+1.',
 'Inside shift x−4 moves the input from 2 to 6.|The output becomes 2×3+1=7.|The transformed point is (6,7).','(6,7)',
 'If (1,4) is on f, find the new y-coordinate on y=3f(x)+2.',14,'',
 'The transformation y=f(x−5) shifts the graph…','5 units right|5 units left|5 units upward|5 units downward',0,'The same original input is reached when x is five larger.')
L('A6.2','Inverse and composite functions',True,'graph','(f∘g)(x)=f(g(x))',
 'Composition means one function’s output becomes another’s input. Apply the inner function first and check that its outputs belong to the outer function’s domain.|An inverse reverses a one-to-one mapping. Its graph reflects the original across y=x; the original domain and range exchange roles.|A function such as x² needs a restricted domain before it can have an inverse function. The reciprocal 1/f(x) is not the inverse f⁻¹(x).',
 'For a composition, substitute the entire inner expression.|For an inverse, write y=f(x), swap x and y, and solve.|Check one-to-one behavior and domain restrictions.|Verify by composing the inverse and original.',
 'For f(x)=2x+3, find f⁻¹(x).',
 'Write y=2x+3.|Swap to x=2y+3.|Solve to y=(x−3)/2.','f⁻¹(x)=(x−3)/2',
 'If f(x)=2x+3 and g(x)=x², calculate f(g(2)).',11,'',
 'What is generally true of f⁻¹ and f?','Their domains and ranges exchange|f⁻¹(x)=1/f(x)|Every function has an inverse function on its original domain|Their graphs are identical',0,'An inverse swaps inputs and outputs, hence domain and range.')
L('B1.1','Rounding, significant figures and error bounds',False,'basic','Lower = a−u/2; upper = a+u/2',
 'A rounded measurement represents an interval of possible original values. The rounding unit u is 1 for a whole number and 0.1 for one decimal place.|The lower bound is usually included and the upper bound excluded under the common half-up rounding convention. Write an inequality rather than replacing the measurement by an unjustified exact value.|For a positive quotient, its greatest possible value uses the numerator’s upper bound and denominator’s lower bound. Relative error compares the absolute error with the true or stated reference value.',
 'Identify the rounding unit.|Take half the unit.|Subtract and add it to obtain bounds.|For a combined calculation, choose extreme values carefully.',
 'A length is 7.2 cm to the nearest 0.1 cm. State the bounds.',
 'The rounding unit is 0.1 cm.|Half a unit is 0.05 cm.|The original length lies from 7.15 inclusive to 7.25 exclusive.','7.15 ≤ L < 7.25 cm',
 'A length is 12.4 cm to the nearest 0.1 cm. Find its lower bound.',12.35,'cm',
 'If 5.0 is rounded to the nearest 0.1, what is its upper bound?','5.05|5.1|5.5|5.00',0,'Half of 0.1 is 0.05, so the upper bound is 5.05.')
L('B1.2','Standard form and percentage error',False,'basic','Percentage error = |approx−reference|/|reference| ×100',
 'Standard form writes a nonzero quantity as a×10ⁿ with 1≤|a|<10. It separates scale from significant digits and is useful for very large or small measurements.|A calculator’s E notation means a power of ten; 2.3E−4 is 0.00023, not 2.3 raised to −4.|Absolute error has the measurement’s units. Percentage error is dimensionless and uses the reference value in the denominator, not whichever number is largest.',
 'Convert each value to a consistent unit.|Find the absolute difference.|Divide by the absolute reference value.|Multiply by 100 and round only at the end.',
 'An estimate is 48 when the reference is 50. Find percentage error.',
 'Absolute error=|48−50|=2.|Relative error=2/50=0.04.|Multiply by 100 to get 4%.','4%',
 'An estimate is 63 and the reference is 60. Find percentage error.',5,'percent',
 'What is 3.2E−3?','0.0032|3200|0.032|−3.2',0,'E−3 multiplies 3.2 by one thousandth.')
L('B2.1','Arithmetic sequences and sums',False,'sequence','uₙ=u₁+(n−1)d; Sₙ=n(u₁+uₙ)/2',
 'An arithmetic sequence has a constant difference between successive terms. Its graph against the integer term number lies on a straight line.|The nth term contains n−1 differences because the first term already exists before any step is taken. This prevents a frequent off-by-one error.|The sum is the number of terms multiplied by their average. It is not simply n times the final term.',
 'Identify the first term and common difference.|Use n−1 steps for the nth term.|For a sum, determine the last term first.|Check whether the context permits only positive terms.',
 'For 7,11,15,… find u₁₀ and S₁₀.',
 'The first term is 7 and the difference is 4.|u₁₀=7+9×4=43.|S₁₀=10(7+43)/2=250.','u₁₀=43; S₁₀=250',
 'The first term is 5 and the difference is 3. Find the 12th term.',38,'',
 'Which feature identifies an arithmetic sequence?','Constant difference|Constant ratio|Constant product of adjacent terms|Every term must be positive',0,'Equal additive steps define an arithmetic sequence.')
L('B2.2','Geometric sequences and finite sums',False,'sequence','uₙ=u₁rⁿ⁻¹; Sₙ=u₁(1−rⁿ)/(1−r)',
 'A geometric sequence multiplies by a constant ratio. It models compound growth, repeated percentage decay and many staged processes.|The nth term has n−1 multiplications. In the finite-sum formula r=1 is a special case: the sum is simply n times the first term.|Growth factors are not percentages. A 12% increase uses r=1.12; a 12% decrease uses r=0.88.',
 'Divide a term by the previous term to find r.|Use n−1 powers in the nth term.|Use the finite-sum formula only when r≠1.|Check whether you need one term or a cumulative sum.',
 'For 3,6,12,… find the sixth term and the sum of the first six.',
 'The ratio is 2.|u₆=3×2⁵=96.|S₆=3(2⁶−1)/(2−1)=189.','96 and 189',
 'A geometric sequence starts at 4 with ratio 3. Find the fifth term.',324,'',
 'A quantity decreases by 8% each step. What ratio applies?','0.92|0.08|1.08|−0.08',0,'The remaining fraction is 1−0.08=0.92.')
L('B3.1','Compound interest and depreciation',False,'finance','FV=PV(1+r/k)ᵏⁿ',
 'Compound interest earns interest on previous interest. Divide the annual nominal rate by the number of compounding periods, and count all those periods.|Depreciation uses the same multiplicative structure with a factor below one. Linear depreciation is a different assumption with a fixed amount removed per period.|Compare nominal rates only after accounting for compounding frequency. State currency and avoid rounding intermediate balances.',
 'Express the annual percentage rate as a decimal.|Divide by compounding frequency k.|Use kn total periods.|Calculate the final balance and interpret interest separately.',
 'Invest €1000 at 4% compounded annually for 3 years.',
 'The annual multiplier is 1.04.|FV=1000×1.04³=1124.864.|The balance is €1124.86 and interest is €124.86.','€1124.86',
 'A €2000 asset loses 20% annually. Find its value after 2 years.',1280,'euros',
 'What makes compound interest different from simple interest?','Interest can itself earn interest|The percentage is added directly to the balance|The balance must always decrease|No time interval is needed',0,'Each new period uses the updated balance.')
L('B3.2','Annuities, loans and finance solvers',False,'finance','Balanceₙ = PV(1+i)ⁿ + PMT((1+i)ⁿ−1)/i',
 'An annuity consists of equal payments at regular intervals. A loan combines an initial balance, interest and recurring repayments.|Finance solvers use a cash-flow sign convention: money paid and money received must have opposite signs. A positive PV and negative PMT are a common loan setup.|Payment timing matters: end-of-period and beginning-of-period payments are not identical. Use consistent payment and compounding periods, and specify the value you are solving for.',
 'Identify N, annual rate, PV, PMT and FV.|Set payments per year and compounding per year.|Choose END or BEGIN.|Use opposite signs for cash entering and leaving; solve and interpret.',
 'At zero interest, repay a €1200 loan over 12 equal monthly payments.',
 'No interest changes the balance.|The total 1200 is split into 12 payments.|Payment magnitude=1200/12=100 euros.','€100 monthly',
 'With no interest, repay €2400 over 24 equal months. Find the payment magnitude.',100,'euros',
 'In a loan solver, why are PV and PMT often opposite signs?','They describe opposite cash-flow directions|One of them must be an error|Negative payments mean no repayment|All finance inputs must be positive',0,'Receiving the loan and making repayments have opposite directions.')
L('B4.1','Exponents and solving growth models',False,'intersection','aᵐaⁿ=aᵐ⁺ⁿ',
 'Index laws organise repeated multiplication. Fractional powers represent roots, while negative powers represent reciprocals.|For a 2029 SL course, solve exponential equations numerically with graphs or a solver rather than treating logarithm manipulation as an SL requirement.|A growth-time answer may be a real number mathematically, but a question asking for the first whole year requires rounding up and checking the inequality.',
 'Write both sides using consistent units.|Graph the growth model and target.|Find the relevant intersection.|Check an integer threshold by substitution.',
 'A value doubles every 3 years. What is its growth factor over 6 years?',
 'Six years contains two doubling intervals.|The factor is 2².|The value becomes four times the starting amount.','Factor 4',
 'A quantity triples every 2 years. What multiplier applies after 6 years?',27,'',
 'In the 2029 SL course, how can a growth-time equation be solved?','Graph the model and target and find their intersection|Assume time must equal the growth rate|Always divide target by rate|Ignore units',0,'Numerical intersection finds the input reaching the target without requiring logarithm algebra.')
L('B4.2','Logarithms and continuous growth',True,'basic','ln(eˣ)=x; P=P₀eᵏᵗ',
 'A logarithm answers which exponent produces a given positive value. Natural logarithms use base e and are useful for continuous growth models.|Logarithms require positive arguments in real arithmetic. The logarithm of a product is a sum of logarithms, but the logarithm of a sum does not split that way.|For continuous growth, k is not generally the same as a discrete percentage rate. The factor over a time interval t is eᵏᵗ.',
 'Isolate the exponential expression.|Take a suitable logarithm on both sides.|Use the power law to bring down the exponent.|Check the argument is positive and interpret time.',
 'Solve 100e⁰·²ᵗ=200.',
 'Divide by 100 to get e⁰·²ᵗ=2.|Take ln to obtain 0.2t=ln2.|t=ln2/0.2≈3.47.','t≈3.47',
 'Solve eˣ=e³. Give x.',3,'',
 'Which logarithm rule is valid for positive a,b?','ln(ab)=ln a+ln b|ln(a+b)=ln a+ln b|ln(a/b)=ln a/ln b|ln(a²)=ln a+2',0,'The logarithm converts multiplication into addition.')
L('B5.1','Matrices and simultaneous equations',True,'matrix','AX=B; X=A⁻¹B if A is invertible',
 'A matrix stores an ordered rectangular array. Matrix multiplication combines rows with columns, and dimensions determine whether an operation is defined.|For a square coefficient matrix A with nonzero determinant, multiplying by its inverse can solve a linear system. The order matters: generally AB is not BA.|A singular matrix has no inverse. A solver must then distinguish an inconsistent system from one with infinitely many solutions; a calculator error alone is not an explanation.',
 'Write equations with variables in the same order.|Build coefficient matrix A and constant column B.|Check invertibility.|Calculate A⁻¹B and verify every original equation.',
 'Solve x+y=5 and 2x−y=1.',
 'Add equations to obtain 3x=6.|Then x=2.|Substitute into x+y=5 to get y=3.','x=2, y=3',
 'Solve x+y=9 and x−y=3. Give x.',6,'',
 'If a square matrix has determinant zero, it is…','Non-invertible|Always the identity|Always all zero|Guaranteed to have a unique solution',0,'A zero determinant means the matrix has no inverse.')
L('B5.2','Transition matrices and long-term states',True,'matrix','vₙ₊₁ = Pvₙ (column convention)',
 'A transition matrix models movements between states. Under a column-vector convention, each column gives the probabilities of moving from one initial state to every possible next state.|Each column must sum to one and probabilities must be non-negative. Some courses use row vectors instead; the convention changes the matrix orientation and multiplication order.|A stationary distribution is unchanged by another step. It solves Pv=v together with entries summing to one, but convergence also depends on the transition structure.',
 'State the vector convention.|Check all probabilities and column sums.|Multiply in the correct order for each step.|For a stationary state solve Pv=v and normalise.',
 'P has columns (0.8,0.2) and (0.3,0.7). Start with v=(100,0). Find the next state.',
 'Use a column vector for the starting counts.|Pv=(0.8×100+0.3×0, 0.2×100+0.7×0).|The next counts are (80,20).','(80,20)',
 'P has columns (0.8,0.2) and (0.3,0.7). With column-vector starting state (0,100), how many are in the first state after one step?',30,'',
 'For a column-stochastic transition matrix, which totals must equal 1?','Each column|Every diagonal|Each individual entry|The determinant',0,'Each column lists all destinations from one starting state.')
L('C1.1','Coordinate geometry and perpendicular lines',False,'graph','m=(y₂−y₁)/(x₂−x₁); m₁m₂=−1 for finite perpendicular slopes',
 'Gradient measures vertical change per horizontal change. A vertical line has undefined gradient, so it must be handled separately.|Parallel nonvertical lines have equal gradients. Perpendicular finite nonzero gradients are negative reciprocals; a horizontal line is perpendicular to a vertical line.|Distance and midpoint formulas apply to coordinates in a consistent scale. Unequal axis scales can make a sketch misleading.',
 'Find the gradient from the coordinates.|Use a negative reciprocal for a perpendicular line where appropriate.|Use point-slope form.|Check by substitution and consider vertical/horizontal special cases.',
 'Find the gradient of the perpendicular to y=2x+5.',
 'The given line has gradient 2.|A perpendicular gradient m satisfies 2m=−1.|Thus m=−1/2.','−0.5',
 'Find the gradient from (1,2) to (5,10).',2,'',
 'Which line is perpendicular to a horizontal line?','A vertical line|Another horizontal line|Every diagonal line|No line',0,'Horizontal and vertical directions meet at a right angle.')
L('C1.2','Voronoi regions and nearest facilities',False,'geometry','Boundary: equal distances to two sites',
 'A Voronoi region contains points nearest to one site. A shared boundary between two sites lies on their perpendicular bisector.|The diagram assumes distance is measured directly in the plane. Roads, barriers and travel speeds can make straight-line proximity an unsuitable service-location model.|A vertex is equidistant from at least three sites. For a point on a boundary, there can be a tie, so nearest-site assignments require an explicit policy.',
 'Plot all site coordinates.|Construct pairwise perpendicular bisectors.|Keep boundary segments that define nearest-site regions.|Explain the distance metric and limitations.',
 'Sites are at (0,0) and (6,0). Find their Voronoi boundary.',
 'The midpoint is (3,0).|The segment joining sites is horizontal.|Its perpendicular bisector is vertical through x=3.','x=3',
 'Sites lie at (0,0) and (10,0). What is the x-coordinate of their boundary?',5,'',
 'A Voronoi boundary between two sites is part of their…','Perpendicular bisector|Connecting line only|Common tangent|Regression line',0,'Its points have equal distances to the two sites.')
L('C2.1','Area, surface area and volume',False,'geometry','V(cylinder)=πr²h; A(sphere)=4πr²',
 'Area measures a two-dimensional region; volume measures three-dimensional space. Their units are squared and cubed, respectively.|A composite solid can be decomposed into familiar shapes. Decide whether a shared face is internal before including it in exposed surface area.|When every length scales by k, area scales by k² and volume by k³. This relationship is useful for checking the plausibility of an answer.',
 'Draw and label dimensions in consistent units.|Identify whether area, exposed surface area or volume is required.|Substitute the correct radius, not the diameter.|Give squared or cubed units.',
 'Find the volume of a cylinder of radius 3 cm and height 5 cm.',
 'Use V=πr²h.|V=π×9×5=45π.|This is approximately 141 cm³.','45π cm³',
 'A cuboid is 3 cm by 4 cm by 5 cm. Find its volume.',60,'cm³',
 'If all lengths double, volume multiplies by…','8|2|4|6',0,'Three-dimensional scaling gives 2³=8.')
L('C2.2','Circles, arcs and sectors',False,'trig','Arc=rθ; sector area=½r²θ (radians)',
 'A radian is defined by arc length divided by radius. A complete circle has angle 2π radians, corresponding to 360 degrees.|For radians the arc and sector formulas are compact. For degrees multiply the full circumference or area by θ/360 instead.|Check the angle unit before entering trigonometric functions. A sector perimeter includes two radii as well as the arc.',
 'Determine whether the angle is in degrees or radians.|Use the matching arc or area formula.|Include straight edges when finding perimeter.|State units and round at the end.',
 'Find the arc length for radius 6 cm and angle 60°.',
 'Convert 60° to π/3 radians.|Arc length=6×π/3.|The length is 2π cm, about 6.28 cm.','2π cm',
 'A circle has radius 4 cm and a sector angle of 0.5 radians. Find the arc length.',2,'cm',
 'Which formula assumes the angle is in radians?','Arc length=rθ|Area of circle=πr²|Circumference=2πr|Diameter=2r',0,'The proportionality s=rθ uses the radian definition.')
L('C3.1','Right triangles, sine and cosine rules',False,'trig','a/sin A=b/sin B; c²=a²+b²−2ab cos C',
 'Right-triangle trigonometry relates an acute angle to ratios of side lengths. For a non-right triangle, the sine and cosine rules provide more general relationships.|The cosine rule is useful with two sides and their included angle, or with all three sides. The sine rule requires a known opposite side-angle pair.|Inverse sine can give an ambiguous second possible angle. Check the triangle’s total angle and the geometry rather than accepting only the first calculator output.',
 'Sketch and label opposite side-angle pairs.|Choose the rule that matches the known information.|Check calculator degree/radian mode.|Validate angle sums and sensible side lengths.',
 'Two sides are 5 and 7 with included angle 60°. Find the opposite side.',
 'c²=5²+7²−2×5×7cos60°.|c²=25+49−35=39.|c=√39≈6.24.','Approximately 6.24',
 'In a right triangle the legs are 6 and 8. Find the hypotenuse.',10,'',
 'When are two sides and their included angle especially suited to the cosine rule?','When finding the third side|Only when the angle is 90°|Only when all sides are equal|Never',0,'The included angle appears directly in c²=a²+b²−2ab cos C.')
L('C3.2','Bearings and three-dimensional trigonometry',False,'trig','Bearing: clockwise from north',
 'A bearing is an angle measured clockwise from north and commonly written with three digits. Bearings are not measured from the positive x-axis.|In a 3D problem first find a suitable horizontal distance, then form the vertical right triangle for an angle of elevation or depression.|A diagram should distinguish plan-view directions from vertical angles. All distances must use compatible units and refer to the same points.',
 'Draw north at the relevant starting point.|Mark the bearing clockwise.|Find a horizontal or planar distance.|Use the resulting right triangle for vertical quantities.',
 'A point is 30 m horizontally away and 40 m above you. Find the line-of-sight distance.',
 'The horizontal and vertical distances are perpendicular.|Use d²=30²+40²=2500.|Take the positive square root to obtain 50 m.','50 m',
 'A displacement is 12 m east and 5 m north. Find its magnitude.',13,'m',
 'How is a bearing measured?','Clockwise from north|Anticlockwise from east|Always from the destination|Only between 0° and 90°',0,'The standard bearing convention starts at north and rotates clockwise.')
L('C4.1','Vectors, magnitude and scalar product',True,'vector','a·b=|a||b|cosθ',
 'A vector has both magnitude and direction. Its components describe changes along the coordinate axes, so vector subtraction gives displacement between positions.|The scalar product combines corresponding components and gives a scalar. It measures directional agreement and can determine the angle between nonzero vectors.|Perpendicular nonzero vectors have dot product zero. The removed vector-product topic is deliberately excluded from this 2029 course.',
 'Write components consistently.|Find magnitudes using sums of squares.|Compute the scalar product.|Use inverse cosine for an angle, checking the interval and angle mode.',
 'Find the magnitude of a=(3,4,12).',
 '|a|=√(3²+4²+12²).|The sum of squares is 169.|The magnitude is 13.','13',
 'Find the dot product of (1,2,3) and (4,0,−1).',1,'',
 'Two nonzero vectors with zero scalar product are…','Perpendicular|Always equal|Always parallel|Always unit vectors',0,'From a·b=|a||b|cosθ, cosθ=0 and θ=90°.')
L('C4.2','Vector lines and motion',True,'vector','r=a+tb',
 'A vector line starts from a position vector a and moves along a direction vector b. The parameter is not necessarily time unless the context defines it that way.|For constant velocity, position equals initial position plus time multiplied by velocity. Components must use consistent distance and time units.|Two motion paths can intersect without the objects colliding: a collision requires the same position at the same time.',
 'Identify initial position and direction or velocity.|Write all components using the same parameter.|Solve matching coordinate equations.|For a collision, check the time value agrees in every coordinate.',
 'An object starts at (1,2) with velocity (3,−1) m/s. Find its position at t=4 s.',
 'Use r=(1,2)+4(3,−1).|The component changes are (12,−4).|The final position is (13,−2).','(13,−2) m',
 'An object starts at x=2 and moves at 5 m/s. Find x after 6 s.',32,'m',
 'For a collision between two moving particles, what must hold?','Same position at the same time|Paths cross somewhere at any times|Equal speeds only|Equal distances travelled only',0,'A path intersection alone does not guarantee simultaneous arrival.')
L('C5.1','Graphs, shortest paths and spanning trees',True,'network','A tree with n vertices has n−1 edges',
 'A graph models connections using vertices and edges. An edge weight can represent cost, distance or time; specify which before optimizing.|A shortest path connects two designated vertices with minimum total weight. A minimum spanning tree instead connects every vertex with minimum total edge weight and no cycles.|Kruskal’s algorithm selects available edges from lightest upward while refusing cycles. Dijkstra’s algorithm solves shortest paths for non-negative edge weights.',
 'State what vertices, edges and weights mean.|Distinguish a path task from a spanning-tree task.|Apply an appropriate algorithm and record chosen edges.|Check connectivity, absence of cycles and the total weight.',
 'A triangle has edge weights AB=3, BC=4 and AC=10. Find the shortest A-to-C distance.',
 'The direct edge costs 10.|The route A-B-C costs 3+4=7.|The shorter route has total weight 7.','7 via B',
 'A spanning tree connects 8 vertices. How many edges does it have?',7,'',
 'A minimum spanning tree aims to…','Connect every vertex at minimum total weight without cycles|Find just the shortest A-to-B route|Use every edge|Maximize the number of cycles',0,'The task spans all vertices using an acyclic connected subgraph.')
L('C5.2','Eulerian routes, route inspection and travelling salesman',True,'network','Euler circuit: all non-isolated vertices even degree in a connected graph',
 'An Eulerian route uses every edge once; a Hamiltonian cycle visits every vertex once before returning to its start. These are different optimization settings.|A route-inspection problem covers all edges at minimum total cost. On a connected undirected graph, pair odd-degree vertices with repeated shortest paths to make an Euler circuit.|The travelling salesman problem seeks a shortest Hamiltonian cycle. Bounds can be more practical than proving an optimal route in a large network.',
 'Decide whether all edges or all vertices must be visited.|Count odd-degree vertices for route inspection.|Find least-cost duplicated paths if required.|For travelling-salesman bounds, state why the bound is valid.',
 'A connected route network has total edge weight 30 and only two odd vertices, 5 apart by shortest path. Find the minimum closed inspection length.',
 'All original edges must be covered, costing 30.|Repeat the shortest path joining the two odd vertices, costing 5.|The closed route length is 35.','35',
 'Original edge total is 42 and two odd vertices are 6 apart. Find the minimum closed inspection length.',48,'',
 'An Euler circuit is about visiting every…','Edge exactly once|Vertex exactly once|Odd vertex only|Shortest path twice',0,'Eulerian traversal concerns edges, whereas Hamiltonian traversal concerns vertices.')
L('D1.1','Sampling, bias and data types',False,'stats','Sample statistic estimates a population parameter',
 'A population is the complete group of interest; a sample is the observed subset. Good sampling aims to represent the population rather than merely to collect a large number.|Quantitative data may be discrete counts or continuous measurements; categorical data describe groups. The variable type determines appropriate summaries and displays.|A large convenience sample can still be biased. Separate selection bias, response bias and measurement problems when evaluating a study.',
 'Define the population and sampling frame.|Identify the sampling method.|Classify variables.|Explain a specific possible bias and its likely consequence.',
 'A school of 600 students samples 10% of its students. Find the sample size.',
 'Ten percent is 0.10.|Multiply 600 by 0.10.|The sample should contain 60 students.','60',
 'A population has 840 members and a sample takes 5%. Find its size.',42,'',
 'Which is a continuous variable?','Measured time to run 100 m|Number of pets|Favourite subject|Number of siblings',0,'Time can in principle take any value within an interval.')
L('D1.2','Mean, median, quartiles and spread',False,'stats','Mean=Σfx/Σf; IQR=Q₃−Q₁',
 'The mean uses every value and is sensitive to extreme observations. The median locates the middle and is often more stable in a skewed distribution.|Quartiles describe the middle half of the data through the interquartile range. Calculator quartile conventions can differ for small samples, so use the course’s stated convention consistently.|Population standard deviation divides squared deviations by n; sample standard deviation uses n−1. A calculator usually labels them σx and Sx, respectively.',
 'Enter values and frequencies in the correct lists.|Check the data count.|Choose mean or median with a reason.|Distinguish sample and population spread and include units.',
 'Find the mean and median of 2,4,4,6,9.',
 'The sum is 25 and n=5, so mean=5.|The ordered middle value is 4.|The larger 9 pulls the mean above the median.','Mean 5; median 4',
 'Data are 3,5,7,9. Find the mean.',6,'',
 'Which calculator output normally uses n−1?','Sx, sample standard deviation|σx, population standard deviation|x̄, the mean|n, the data count',0,'Sx estimates population spread using the sample correction n−1.')
L('D1.3','Box plots, cumulative frequency and outliers',False,'stats','Outlier fences: Q₁−1.5IQR and Q₃+1.5IQR',
 'A box plot displays median, quartiles and whiskers. A modified box plot marks outliers separately; its whiskers do not necessarily extend to the overall minimum and maximum.|Cumulative frequency adds counts up to a value. To estimate a percentile, start with its proportion of the total count and read the corresponding value.|Compare distributions using both centre and spread in context. A higher median is not the same as greater consistency.',
 'Identify median and quartiles.|Compute IQR and outlier fences.|For grouped cumulative data, read values as estimates.|Compare centre and spread with units and context.',
 'Q₁=10 and Q₃=18. Find the upper outlier fence.',
 'IQR=18−10=8.|1.5IQR=12.|The upper fence is 18+12=30.','30',
 'If Q₁=6 and Q₃=14, find the lower outlier fence.',-6,'',
 'In a modified box plot a separated dot usually represents…','An outlier|The median|The sample mean|The lower quartile',0,'Outliers are drawn individually beyond the modified whiskers.')
L('D2.1','Pearson correlation and linear regression',False,'regression','ŷ=ax+b; residual=y−ŷ',
 'Pearson’s r measures the direction and strength of a linear association. It lies from −1 to 1, but a value near zero does not rule out a nonlinear relationship.|The regression of y on x predicts y from x by minimizing squared vertical residuals. Reversing the roles of variables generally gives a different fitted line.|Correlation does not establish causation. Hidden variables, reverse direction and chance can explain a relationship. Predictions far outside the data interval are extrapolations.',
 'Enter paired x and y lists in matching order.|Draw a scatter plot and check for unusual values.|Fit the regression and inspect r and residuals.|Use the correct prediction direction and interpret units.',
 'For ŷ=2x+3 and observed (4,12), find the residual.',
 'Predicted y is 2×4+3=11.|Residual=observed−predicted.|The residual is 12−11=1.','1',
 'A regression predicts ŷ=3x−2. Find the prediction at x=5.',13,'',
 'A strong correlation by itself proves…','Association, not causation|That x causes y|That y causes x|No possible confounding',0,'A statistical association alone cannot establish a causal mechanism.')
L('D2.2','Rank correlation and model evaluation',True,'regression','Spearman rₛ = correlation of ranks',
 'Spearman rank correlation measures monotonic association using ranks. It can be useful when the relationship is increasing or decreasing without being linear.|Tied values receive average ranks. Applying the no-ties shortcut without adjusting for ties can give a wrong result; correlation of the ranked lists is safer.|The coefficient of determination describes variation accounted for by a fitted model in an appropriate setting. A high value does not prove causation or guarantee safe extrapolation.',
 'Assign ranks consistently to both variables.|Give tied values their mean rank.|Correlate the two rank lists.|Interpret direction, strength and limitations.',
 'Three values 10,10,30 occupy ranks 1,2,3. Assign ranks.',
 'The two 10s tie for ranks 1 and 2.|Their average rank is 1.5.|The 30 retains rank 3.','1.5, 1.5, 3',
 'Two tied observations occupy ranks 4 and 5. What rank should each receive?',4.5,'',
 'Which description best suits Spearman correlation?','Strength of monotonic association using ranks|Always the gradient of a regression line|Only valid for normally distributed raw data|Proof of causation',0,'Ranking permits assessment of a monotonic rather than necessarily linear pattern.')
L('D3.1','Probability rules and conditional probability',False,'probability','P(A|B)=P(A∩B)/P(B)',
 'Conditional probability changes the sample space to cases where the condition holds. The denominator therefore refers to the conditioning event, not the entire original group.|Mutually exclusive events cannot both occur; independent events do not change each other’s probabilities. These definitions are different.|For a union, add individual probabilities and subtract the overlap once. A tree diagram multiplies along a branch and adds distinct complete paths.',
 'Define the events and the conditioning information.|Use a table, Venn diagram or tree.|Choose a denominator matching the restricted group.|Check the answer lies between 0 and 1.',
 'P(A∩B)=0.12 and P(B)=0.30. Find P(A|B).',
 'Restrict the sample space to B.|Divide the overlap by P(B).|0.12/0.30=0.40.','0.40',
 'P(A∩B)=0.18 and P(B)=0.60. Calculate P(A|B).',0.3,'',
 'Independent events satisfy…','P(A∩B)=P(A)P(B)|P(A∩B)=0 in every case|P(A)+P(B)=1 always|P(A given B)=0 always',0,'Multiplication of marginal probabilities characterizes independence.')
L('D3.2','Tree diagrams and Bayes reasoning',True,'probability','P(A|B)=P(B|A)P(A)/P(B)',
 'Bayes reasoning reverses conditioning by accounting for base rates. A positive test can have a lower predictive probability when the tested condition is rare.|Use a complete probability tree: multiply along each path and add all paths giving the observed result to form the denominator.|Sensitivity and specificity condition on true status; positive predictive value conditions on a positive result. Confusing these quantities is a common interpretation error.',
 'List base rates for each starting group.|Multiply by conditional probabilities.|Add all paths reaching the evidence.|Divide the desired joint probability by total evidence probability.',
 'Half a group uses method A. Success rates are 0.8 with A and 0.6 without. Find the probability of success.',
 'P(A and success)=0.5×0.8=0.4.|P(not A and success)=0.5×0.6=0.3.|Total success probability=0.7.','0.7',
 'P(A)=0.4, P(B|A)=0.5 and P(B)=0.25. Find P(A|B).',0.8,'',
 'Why can a positive test be misleading for a rare condition?','False positives may outnumber true positives|Sensitivity always equals zero|Base rates cannot affect results|Specificity and predictive value are identical',0,'Bayes reasoning weighs test results by the size of the underlying groups.')
L('D4.1','Discrete random variables and expectation',False,'stats','E(X)=ΣxP(X=x)',
 'A random variable assigns a number to an outcome. A discrete distribution lists possible values and probabilities that sum to one.|Expected value is a probability-weighted mean, not necessarily a possible outcome. Over many repetitions it describes the long-run average under the model.|For a game, subtract any entry fee from the expected payout to obtain expected net gain. A fair game has expected net gain zero, not necessarily equal winning chances.',
 'Check probabilities are non-negative and total one.|Multiply each value by its probability.|Add the contributions.|Interpret the expected value with units and any costs.',
 'A payout is 0 with probability 0.7 and 10 with probability 0.3. Find its expectation.',
 'E(X)=0×0.7+10×0.3.|The weighted sum is 3.|The long-run average payout is 3 currency units.','3',
 'X is 2 with probability 0.4 and 7 with probability 0.6. Calculate E(X).',5,'',
 'Must an expected value be a possible observation?','No, it is a weighted average|Yes, always|Only if all probabilities are unequal|It must be the largest value',0,'For example, a discrete average can lie between possible outcomes.')
L('D4.2','Binomial distribution and inequalities',False,'binomial','X~B(n,p); E(X)=np; Var(X)=np(1−p)',
 'A binomial model counts successes in a fixed number of independent trials with the same success probability. Check these assumptions before choosing the distribution.|The probability mass function gives exactly one count; the cumulative function gives a range of counts. On the TI-84, binomcdf(n,p,k) includes all values from zero through k.|For at least k, subtract P(X≤k−1) from one. For between a and b inclusive, subtract P(X≤a−1) from P(X≤b).',
 'Define success and state n and p.|Translate words into an inequality.|Choose pdf for exactly or cdf for a cumulative range.|Write the probability notation and interpret the result.',
 'For X~B(10,0.3), find E(X) and write P(X≥4) for calculator evaluation.',
 'E(X)=10×0.3=3.|P(X≥4)=1−P(X≤3).|Use 1−binomcdf(10,0.3,3) on the TI-84.','Mean 3; upper-tail complement at 3',
 'For X~B(20,0.25), find the variance.',3.75,'',
 'Which TI-84 expression gives P(X≥5)?','1−binomcdf(n,p,4)|binomcdf(n,p,5)|binompdf(n,p,5)|1−binomcdf(n,p,5)',0,'The excluded lower counts are 0 through 4, not through 5.')
L('D4.3','Normal distribution and inverse normal',False,'normal','Z=(X−μ)/σ',
 'A normal distribution is continuous, symmetric and bell-shaped. Its mean sets the centre and its standard deviation sets the spread; variance is σ².|Probabilities are areas under the density curve. The probability of one exact continuous value is zero, so normalpdf is not a probability of equality.|Normalcdf finds an area from bounds. Inverse normal finds a boundary from a known area; check whether the input area is to the left or right.',
 'State the mean and standard deviation.|Sketch and shade the required region.|Use normalcdf for an interval or inverse normal for a percentile.|Check symmetry and the scale of the answer.',
 'For X~N(50,8²), write a calculator expression for P(42<X<58).',
 'The bounds are one standard deviation below and above 50.|Use normalcdf(42,58,50,8).|The probability is approximately 0.6827.','Approximately 0.683',
 'For a normal variable with mean 70 and standard deviation 5, find the z-score of 80.',2,'',
 'In N(50,8²), what standard deviation enters normalcdf?','8|64|50|√8',0,'The second distribution parameter is variance, but the calculator requests standard deviation.')
L('D4.4','Continuous densities and linear combinations',True,'integral','P(a<X<b)=∫ₐᵇf(x)dx; Var(aX+b)=a²Var(X)',
 'A probability density is non-negative and has total area one. Its height can exceed one because probability is area, not height.|A linear transformation shifts and scales a random variable. Means transform linearly; variance scales with the square of a multiplier and is unchanged by adding a constant.|For independent variables, variances add even for a difference. Dependence introduces covariance, so independence must not be assumed silently.',
 'Check support and total density area.|Integrate over the requested interval.|Use expectation and variance rules with clear independence assumptions.|Convert variance back to standard deviation if needed.',
 'A uniform density is 1/4 on 0≤x≤4. Find P(1<X<3).',
 'The requested interval has width 2.|Area=width×height=2×1/4.|The probability is 0.5.','0.5',
 'If Var(X)=9, find Var(2X+5).',36,'',
 'If X and Y are independent, Var(X−Y) equals…','Var(X)+Var(Y)|Var(X)−Var(Y)|0|Var(X)Var(Y)',0,'The minus sign is squared when variances are combined.')
L('D5.1','Hypotheses, p-values and decisions',False,'test','Reject H₀ when p≤α (stated convention)',
 'A statistical test starts with a null hypothesis and an alternative describing a population claim. A p-value measures how surprising the data, or more extreme data, would be if the null model were true.|The significance level is the chosen threshold for rejecting the null. A p-value is not the probability that the null hypothesis is true.|A non-significant result means insufficient evidence against the null, not proof of no effect. Conclusions must return to the population and context.',
 'Write null and alternative hypotheses.|Choose the test and check assumptions.|Compare p with the significance level.|State reject or fail to reject H₀ and give a contextual conclusion.',
 'A test gives p=0.032 at a 5% significance level. State the decision.',
 'Convert 5% to 0.05.|0.032 is less than 0.05.|Reject the null; there is evidence for the stated alternative.','Reject H₀',
 'A p-value is 0.04. Express it as a percentage.',4,'percent',
 'If p=0.21 at α=0.05, the correct decision is…','Fail to reject H₀|Prove H₀ true|Reject H₀|The test has a 21% chance of being correct',0,'The evidence is not strong enough at the chosen significance level.')
L('D5.2','Chi-squared independence and goodness of fit',False,'chi','χ²=Σ(O−E)²/E',
 'A chi-squared test compares observed category counts with expected counts under a null model. Use frequencies rather than percentages without sample counts.|For independence, expected count equals row total times column total divided by the grand total, with degrees of freedom (r−1)(c−1).|A goodness-of-fit test instead compares one categorical distribution with specified proportions. Small expected counts may require pooling categories and revising degrees of freedom.',
 'Identify independence or goodness of fit.|State the null model and calculate expected counts.|Check expected-count conditions and determine degrees of freedom.|Obtain the right-tail p-value and conclude in context.',
 'A table has row total 30, column total 20 and grand total 100. Find the expected cell count.',
 'Under independence use row total×column total/grand total.|E=30×20/100.|The expected frequency is 6.','6',
 'Find degrees of freedom for an independence test with 3 rows and 4 columns.',6,'',
 'Which input is appropriate for a chi-squared test?','Observed category counts|Only group means|Only percentages with no sample sizes|Paired continuous slopes',0,'The statistic compares observed and expected frequencies.')
L('D5.3','Comparing means with a two-sample t-test',False,'test','H₀: μ₁=μ₂',
 'A two-sample t-test compares population means using sample means and estimated variability. It is not a test of whether the raw samples are identical.|Use independent samples only when that design applies. A matched-pairs study needs a different treatment based on within-pair differences.|Check sampling, independence and distributional conditions. If variances are not assumed equal, an unpooled test avoids imposing that extra assumption.',
 'Identify independent groups and the population means.|State a one- or two-sided alternative.|Enter raw data or summary statistics with the correct sample standard deviations.|Report p-value, decision and context without claiming causation.',
 'Group means are 18 and 15. Find the observed difference μ̂₁−μ̂₂.',
 'Keep the order consistent with the hypotheses.|Subtract 15 from 18.|The observed mean difference is 3; significance also requires spread and sample sizes.','3',
 'A sample mean is 23 and the comparison sample mean is 19. Find the observed difference.',4,'',
 'Which extra information is needed beyond two sample means to run a t-test?','Sample sizes and variability|Only the larger maximum|Only the variable names|No other information',0,'Uncertainty in the difference depends on sample spread and size.')
L('D5.4','Confidence intervals and test errors',True,'test','Type I: reject a true H₀; Type II: fail to reject a false H₀',
 'A confidence interval estimates a parameter with a procedure that has a specified long-run coverage. A realised interval either contains the fixed parameter or does not.|Wider intervals can result from higher confidence or greater variability. Increasing sample size generally reduces sampling uncertainty under the same design.|A Type I error rejects a true null. A Type II error misses a false null; power is the probability of rejecting a false null for a specified alternative.',
 'Identify parameter and estimation method.|Check conditions.|Calculate endpoints with an appropriate interval tool.|Interpret coverage and distinguish the two test errors.',
 'A confidence interval is 12±3. State its endpoints.',
 'Subtract the margin from 12 to obtain 9.|Add the margin to 12 to obtain 15.|The interval is [9,15].','[9,15]',
 'An interval is [18,26]. Find its margin of error.',4,'',
 'A Type I error means…','Rejecting a true null hypothesis|Failing to reject a false null hypothesis|Making a calculation typo|Always accepting an alternative',0,'Type I is a false positive decision against a true null.')
L('E1.1','Gradient functions and numerical derivatives',False,'derivative','f′(a) = instantaneous rate of change at a',
 'An average rate measures change across an interval. A derivative describes the limiting rate at a single input, equal to the tangent gradient for a differentiable graph.|A positive derivative means the function is increasing locally; a negative derivative means decreasing. The value of the function and its derivative answer different questions.|A numerical derivative estimates a slope at a point. Record the function and the point of evaluation rather than writing only a calculator number.',
 'Identify the output and input units.|Distinguish interval-average from instantaneous rate.|Differentiate or use numerical differentiation at the requested point.|Interpret the sign and units.',
 'For f(x)=x², find the tangent gradient at x=3.',
 'The derivative is f′(x)=2x.|Substitute x=3.|The tangent gradient is 6.','6',
 'For f(x)=x², find the gradient at x=4.',8,'',
 'If f′(a)<0, the graph near a is…','Decreasing|Necessarily below the x-axis|Necessarily concave down|At a maximum in every case',0,'The sign of the first derivative describes local direction, not height or concavity.')
L('E2.1','Power rule and tangent equations',False,'derivative','d(axⁿ)/dx=anxⁿ⁻¹',
 'The power rule multiplies by the exponent and reduces the exponent by one. A constant term differentiates to zero.|A tangent equation needs both a point on the original graph and a gradient from the derivative. Do not substitute the derivative value as the y-coordinate.|A normal line is perpendicular to the tangent; for a finite nonzero tangent gradient its gradient is the negative reciprocal. Handle horizontal tangents separately.',
 'Differentiate each polynomial term.|Evaluate the derivative at the requested x.|Evaluate the original function for the point.|Use y−y₀=m(x−x₀).',
 'For y=x²+1, find the tangent at x=2.',
 'At x=2, y=5.|The derivative 2x gives slope 4.|The line is y−5=4(x−2), so y=4x−3.','y=4x−3',
 'For f(x)=3x²+2x−7, find f′(2).',14,'',
 'The derivative of a constant 9 is…','0|9|1|9x',0,'A constant has no change as the input changes.')
L('E2.2','Chain, product and quotient rules',True,'derivative','(uv)′=u′v+uv′; (f(g(x)))′=f′(g(x))g′(x)',
 'The chain rule handles a function inside another function. Differentiate the outer rule while keeping its inner expression, then multiply by the inner derivative.|A product is not differentiated by multiplying the separate derivatives. Apply the product rule, which accounts for both changing factors.|The quotient rule has an ordered subtraction in its numerator. Simplify carefully, retain domain restrictions and check a numerical derivative as a separate validation.',
 'Identify the outer and inner functions or product factors.|Choose the matching rule.|Write the full derivative before simplifying.|Check at a point numerically.',
 'Differentiate y=(3x+1)⁴.',
 'The outer derivative is 4(3x+1)³.|The inner derivative is 3.|Multiply to get 12(3x+1)³.','12(3x+1)³',
 'For y=(2x+1)³, calculate y′ at x=1.',54,'',
 'Which derivative of uv is correct?','u′v+uv′|u′v′|u′+v′|uv′−u′v',0,'Both factors can change, so both product-rule terms are needed.')
L('E3.1','Antiderivatives and definite integrals',False,'integral','∫xⁿdx=xⁿ⁺¹/(n+1)+C, n≠−1',
 'An antiderivative reverses differentiation. An indefinite integral represents a family that differs by an additive constant.|A definite integral gives signed accumulation between bounds. For a graph below the axis, its contribution is negative rather than a positive geometric area.|The fundamental theorem evaluates a definite integral by subtracting antiderivative values at the upper and lower bounds. Preserve brackets around each substituted expression.',
 'Find an antiderivative.|For an indefinite integral include C.|For a definite integral evaluate upper minus lower.|Check sign, units and whether an area or signed accumulation was requested.',
 'Evaluate the integral of 2x from 1 to 3.',
 'An antiderivative is x².|Evaluate 3²−1².|The definite integral is 8.','8',
 'Evaluate the integral of 3x² from 0 to 2.',8,'',
 'Why include C in an indefinite integral?','Constants disappear on differentiation|Every integral must be positive|It represents the lower bound|It equals the mean',0,'All antiderivatives differing by a constant have the same derivative.')
L('E3.2','Numerical integration and areas between curves',False,'integral','Area = ∫(upper−lower)dx on each interval',
 'A calculator can evaluate a definite integral numerically even when an elementary antiderivative is inconvenient. You still need the integrand and bounds.|Geometric area is non-negative. If the curves exchange order, split the interval at intersections before integrating upper minus lower.|The 2029 SL course no longer requires the trapezoidal-rule approximation topic; numerical integration here uses the GDC’s definite-integral facility.',
 'Find the relevant intersections.|Identify upper and lower functions on each interval.|Integrate their difference in the correct order.|Add positive pieces and give square units if applicable.',
 'Find the area between y=2 and y=x on 0≤x≤2.',
 'On this interval the constant line is above y=x.|Integrate 2−x from 0 to 2.|[2x−x²/2]₀²=4−2=2.','2 square units',
 'Find the area between y=3 and y=x on 0≤x≤3.',4.5,'square units',
 'What should you do when two boundary curves swap which one is higher?','Split at their intersection|Always use one signed integral and ignore its sign|Use only the upper endpoint|Differentiate both and subtract gradients',0,'Splitting ensures each area contribution uses upper minus lower.')
L('E4.1','Stationary points and optimization',False,'minimum','Stationary point: f′(x)=0',
 'A stationary point has zero first derivative, but it need not be a maximum or minimum. A horizontal inflection is also possible.|For optimization on a closed interval, compare stationary points with endpoints. A calculator’s local minimum tool can miss a global endpoint optimum.|A practical constraint reduces the number of independent variables. Define the domain before solving and interpret a feasible optimum with units.',
 'Write the quantity to optimize in one variable.|State its feasible interval.|Find stationary candidates.|Compare their values with endpoints and interpret.',
 'For f(x)=x²−6x+13, find the minimum.',
 'f′(x)=2x−6, so the stationary point is x=3.|f(3)=9−18+13=4.|Since the quadratic opens upward, the minimum is 4.','Minimum 4 at x=3',
 'Find the x-coordinate of the minimum of x²−8x+20.',4,'',
 'For a global maximum on a closed interval, you must check…','Stationary points and endpoints|Only f′(x)=0|Only x=0|Only the largest root',0,'An endpoint may have a larger value than every stationary point.')
L('E4.2','Kinematics, displacement and distance',True,'integral','v=s′; a=v′; distance=∫|v|dt',
 'Velocity is the derivative of displacement and acceleration is the derivative of velocity. Velocity has direction, whereas speed is its magnitude.|The integral of velocity gives displacement. Total distance needs the integral of speed, so split at sign changes of velocity.|An initial position is needed to recover position from velocity. A definite integral alone gives a change in position, not always the final position.',
 'Keep time units consistent.|Differentiate position or velocity as appropriate.|Find times where velocity changes sign.|Add absolute displacement pieces for total distance.',
 'v(t)=2t−2 on 0≤t≤2. Find displacement and total distance.',
 'The integral [t²−2t]₀² is 0.|Velocity changes sign at t=1.|Distances are 1 on each side, so total distance is 2.','Displacement 0; distance 2',
 'A particle has constant velocity 3 m/s for 4 s. Find the displacement.',12,'m',
 'Total distance travelled is obtained from…','The integral of speed|The signed integral of acceleration|The final velocity alone|The mean position',0,'Integrating |velocity| counts motion in both directions positively.')
L('E4.3','Second derivatives and concavity',True,'derivative','f″(x) = rate of change of gradient',
 'The second derivative describes how the first derivative changes. A positive second derivative means the graph bends upward; it does not necessarily mean the function is increasing.|At a stationary point, a positive second derivative identifies a local minimum and a negative second derivative identifies a local maximum. A zero value leaves that test inconclusive.|An inflection needs a change in concavity. Solving f″(x)=0 only finds candidates; check the signs on either side.',
 'Differentiate twice.|Identify candidate stationary or inflection points.|Test the second derivative or sign changes.|State whether the evidence establishes a maximum, minimum or inflection.',
 'For f(x)=x³, discuss x=0.',
 'f′=3x² and f″=6x.|f″ changes from negative to positive through zero.|The origin is an inflection with horizontal tangent.','Stationary inflection at (0,0)',
 'For f(x)=x³, calculate f″(2).',12,'',
 'If f″=0 at a point, is an inflection guaranteed?','No, concavity must change|Yes, always|Only if the function is positive|It is always a maximum',0,'A zero second derivative is a candidate condition, not a complete classification.')
L('E5.1','Differential equations and initial conditions',True,'derivative','dy/dt=ky ⇒ y=Ceᵏᵗ',
 'A differential equation connects a changing quantity with its rate of change. In proportional growth, the rate depends on how much is currently present.|A general solution contains a constant; an initial condition selects a particular solution. For a model dy/dt=ky, k has inverse-time units.|A differential equation is also a modelling assumption. Unlimited proportional growth or decay may fail when capacity, resources or external inputs matter.',
 'Identify dependent and independent variables.|Read the rate relationship and units.|Find a general solution where possible.|Apply the initial condition and assess the model’s limits.',
 'Solve y′=0.2y with y(0)=10.',
 'The proportional-growth solution is y=Ce⁰·²ᵗ.|At t=0 the exponential is 1, so C=10.|Thus y=10e⁰·²ᵗ.','y=10e⁰·²ᵗ',
 'For y=5e⁰·¹ᵗ, find y′(0).',0.5,'',
 'What does an initial condition do?','Selects a particular solution|Forces all derivatives to zero|Removes the need for a model|Always makes the solution linear',0,'It fixes the arbitrary constant or constants in the solution family.')
L('E5.2','Euler’s method and coupled systems',True,'sequence','yₙ₊₁=yₙ+h f(tₙ,yₙ)',
 'Euler’s method follows a slope field using short tangent steps. At each step the slope is evaluated using the current point, then both time and the dependent variable advance.|A smaller step often improves accuracy but requires more calculations; it does not automatically remove every numerical difficulty. State the step size when reporting an approximation.|For simultaneous differential equations, update all variables using their old values from the start of the step. Updating one variable early can accidentally change the numerical scheme.',
 'Write starting values and step size.|Calculate all slopes at the current state.|Update variables simultaneously.|Repeat the stated number of steps and label the result approximate.',
 'Use one Euler step for y′=y, y(0)=2, h=0.1.',
 'At the initial point the slope is 2.|Increment=h×slope=0.1×2=0.2.|The next approximation is y(0.1)≈2.2.','2.2',
 'For y′=2y, y(0)=3 and h=0.1, find the one-step Euler approximation.',3.6,'',
 'In a coupled Euler step, slopes should use…','All old state values|One new value as soon as it is calculated|Only the final time|Only the largest variable',0,'Simultaneous updates evaluate the vector field at the same old state.')
L('A1.3','Inverse functions and restricting a domain',False,'graph','f⁻¹(f(x))=x on the appropriate domain',
 'An inverse function reverses a mapping, taking an original output back to its input. Its domain is the original range and its range is the original domain.|A function needs to be one-to-one to have an inverse function. For example, x² has two real inputs for most positive outputs unless its domain is restricted.|To find an inverse algebraically, write y=f(x), exchange x and y, then rearrange. On a graph the inverse reflects the original across y=x; it is not the reciprocal 1/f(x).',
 'Check whether each output has only one input.|State a domain restriction if needed.|Swap input and output and rearrange.|Verify by substitution or reflection in y=x.',
 'Find the inverse of f(x)=3x−6.',
 'Write y=3x−6 and swap to x=3y−6.|Add 6 and divide by 3.|The inverse is f⁻¹(x)=(x+6)/3.','f⁻¹(x)=(x+6)/3',
 'If f(x)=4x−8, calculate f⁻¹(12).',5,'',
 'What does f⁻¹ mean?','The mapping reversing f|Always 1/f|The negative of f|The derivative of f',0,'The inverse exchanges the roles of inputs and outputs.')
L('A3.3','Logistic growth and carrying capacity',True,'regression','P(t)=K/(1+A e⁻ᵇᵗ)',
 'A logistic model initially grows but slows as its value approaches a limiting capacity K. Its rate changes with both current population and remaining capacity.|When A and b are positive, the model approaches K from below as time increases. The value at t=0 is K/(1+A), so A is not simply the initial population.|The largest growth rate occurs at the midpoint of the logistic curve under this model. Fitting the model needs data spanning enough of the growth pattern; early data alone may not estimate the capacity reliably.',
 'Identify the limiting capacity and initial value.|Check signs and the contextual domain.|Use a graph or regression for predictions and parameters.|Discuss whether a fixed capacity is a realistic assumption.',
 'For P(t)=1000/(1+9e⁻⁰·²ᵗ), find P(0) and the limiting capacity.',
 'At t=0, the exponential equals 1.|P(0)=1000/(1+9)=100.|As t increases the denominator approaches 1, so the limit is 1000.','Initial 100; capacity 1000',
 'For P(t)=800/(1+3e⁻⁰·¹ᵗ), find P(0).',200,'',
 'In K/(1+A e⁻ᵇᵗ), with A,b positive, what is K?','The upper limiting capacity|The initial population in every case|The fixed annual addition|The time step',0,'As t increases the exponential tends to zero and the model tends to K.')
L('B5.3','Eigenvalues, eigenvectors and matrix powers',True,'matrix','Av=λv for a nonzero eigenvector v',
 'An eigenvector is a nonzero direction that a matrix transformation preserves, possibly reversing or rescaling it. Its eigenvalue gives that scale factor.|For a two-by-two matrix, eigenvalues satisfy det(A−λI)=0. Substituting an eigenvalue lets you solve (A−λI)v=0 for a corresponding nonzero vector.|If enough independent eigenvectors exist, diagonalization A=PDP⁻¹ makes powers easier: Aⁿ=PDⁿP⁻¹. A transition matrix has a stationary direction associated with eigenvalue 1 under the usual stochastic model.',
 'Form A−λI and set its determinant to zero.|Find eigenvalues.|For each value solve the homogeneous vector equation.|Check Av=λv and, before diagonalizing, independence of the eigenvectors.',
 'For A=diag(2,3), show that v=(1,0) is an eigenvector.',
 'Multiply: A(1,0)=(2,0).|This equals 2(1,0).|Therefore the vector has eigenvalue 2.','Eigenvalue 2',
 'For A=diag(4,7), what eigenvalue corresponds to v=(0,1)?',7,'',
 'An eigenvector must be…','Nonzero and satisfy Av=λv|The zero vector only|A matrix inverse|Always a probability vector',0,'The zero vector is excluded because it would satisfy the equation for every λ.')
L('D4.5','Sampling distributions and the central limit idea',True,'normal','E(X̄)=μ; SD(X̄)=σ/√n for independent observations',
 'A sample mean varies from sample to sample. Its sampling distribution describes those means, not the distribution of individual observations.|For independent observations with finite population variance, the standard deviation of the sample mean is σ/√n. It is often called the standard error.|The central limit theorem explains why sample means can be approximately normal for sufficiently large samples even when individual measurements are not. The required sample size depends on skewness and tails; independence remains important.',
 'Distinguish individual observations from sample means.|Identify population mean, standard deviation and sample size.|Calculate σ/√n for the mean’s standard error.|Assess whether a normal approximation is justified; this is not a removed population-mean hypothesis test.',
 'A population has μ=50 and σ=12. Find the mean and standard error of independent samples of size 36.',
 'The sample mean is centred on 50.|Standard error=12/√36.|This gives 12/6=2.','Mean 50; standard error 2',
 'A population standard deviation is 15 and n=25 independent observations. Find the standard error of the sample mean.',3,'',
 'Increasing an independent sample size by a factor of four changes standard error to…','Half its previous value|Four times its previous value|Twice its previous value|Exactly zero',0,'Standard error scales as 1/√n, and √4=2.')

# Every official 2029 subtopic A1–E5 is represented; this is a teaching map, not a claim to full-guide outcome verification.
NUMERIC_SOLUTIONS={'A1.1': 'Substitute −2 with brackets: g(−2)=3(−2)²−2.|Square first: (−2)²=4.|Then 3×4−2=10.', 'A1.2': 'At the intersection, 2x+1=7.|Subtract 1 and divide by 2.|x=6/2=3.', 'A2.1': 'Use C=3d+4 with d=6.|C=3×6+4.|The trip costs €22.', 'A2.2': 'The squared term has minimum 0 at x=3.|Then f(3)=2×0+7.|The minimum output is 7, not the vertex x-coordinate 3.', 'A2.3': 'Substitute x=2: 2×2³−2+1.|Evaluate the power: 2³=8.|Then 16−2+1=15.', 'A3.1': 'Use y=48/x.|Substitute x=8.|48/8=6.', 'A3.2': 'Each year retains 90%, a multiplier of 0.9.|After two years: 500×0.9².|The model gives 405.', 'A4.1': 'Amplitude is half the difference between peak and trough.|Compute (17−5)/2.|The amplitude is 6.', 'A5.1': '7 km exceeds 5, so use 4+2(d−5).|The extra distance is 7−5=2 km.|Fee=4+2×2=€8.', 'A6.1': 'The transformation changes outputs to 3y+2.|The original output is 4.|The new y-coordinate is 3×4+2=14.', 'A6.2': 'Work from the inside: g(2)=2²=4.|Then f(g(2))=f(4)=2×4+3.|The result is 11.', 'B1.1': 'The rounding unit is 0.1 cm.|Half a unit is 0.05 cm.|Lower bound=12.4−0.05=12.35 cm.', 'B1.2': 'Absolute error=|63−60|=3.|Use the reference 60 in the denominator.|Percentage error=3/60×100=5%.', 'B2.1': 'Use uₙ=u₁+(n−1)d.|Substitute u₁=5, d=3, n=12.|u₁₂=5+11×3=38.', 'B2.2': 'Use uₙ=u₁rⁿ⁻¹.|Substitute u₁=4, r=3, n=5.|u₅=4×3⁴=4×81=324.', 'B3.1': 'A loss of 20% means a multiplier of 0.8.|For two years, use 2000×0.8².|The value is €1280.', 'B3.2': 'At zero interest, total repayment equals the starting balance.|Divide 2400 by 24 equal payments.|The payment magnitude is €100 per month.', 'B4.1': 'Six years contains 6/2=3 tripling periods.|The multiplier is 3³.|The quantity is 27 times its initial value.', 'B4.2': 'The exponential with base e is one-to-one.|eˣ=e³ therefore requires equal exponents.|x=3.', 'B5.1': 'Add x+y=9 and x−y=3.|This gives 2x=12.|Divide by 2 to obtain x=6.', 'B5.2': 'Multiply the first matrix row by the initial column vector.|First state=0.8×0+0.3×100.|There are 30 in the first state after one step.', 'C1.1': 'Gradient is change in y divided by change in x.|Compute (10−2)/(5−1).|The gradient is 8/4=2.', 'C1.2': 'The midpoint of the sites has x-coordinate (0+10)/2=5.|Their connecting segment is horizontal.|Its perpendicular bisector is x=5, so the requested coordinate is 5.', 'C2.1': 'Volume of a cuboid is length×width×height.|Compute 3×4×5.|The volume is 60 cm³.', 'C2.2': 'The angle is already in radians.|Use arc length s=rθ.|s=4×0.5=2 cm.', 'C3.1': 'Use Pythagoras for the perpendicular legs.|Hypotenuse=√(6²+8²)=√100.|Take the positive length, 10.', 'C3.2': 'East and north components are perpendicular.|Magnitude=√(12²+5²)=√169.|The displacement magnitude is 13 m.', 'C4.1': 'Multiply matching vector components and add.|1×4+2×0+3×(−1).|The scalar product is 4+0−3=1.', 'C4.2': 'For constant velocity use x=x₀+vt.|Substitute x₀=2, v=5 and t=6.|x=2+5×6=32 m.', 'C5.1': 'A tree with n vertices has n−1 edges.|Substitute n=8.|There are 7 edges.', 'C5.2': 'For a closed route, the two odd vertices need a duplicated connecting path.|Add the shortest such path to the total original weight.|42+6=48.', 'D1.1': 'Five percent is 0.05.|Multiply the population size by this proportion.|840×0.05=42 members.', 'D1.2': 'Add all four values: 3+5+7+9=24.|Divide by the number of observations.|The mean is 24/4=6.', 'D1.3': 'IQR=14−6=8.|The lower fence is Q₁−1.5IQR.|6−1.5×8=−6.', 'D2.1': 'Use the prediction equation ŷ=3x−2.|Substitute x=5.|ŷ=15−2=13.', 'D2.2': 'Tied observations share their average rank.|Average the occupied ranks 4 and 5.|Each rank is (4+5)/2=4.5.', 'D3.1': 'Restrict the denominator to event B.|Use P(A given B)=0.18/0.60.|The conditional probability is 0.30.', 'D3.2': 'The joint probability is P(A)P(B given A)=0.4×0.5=0.2.|Divide the joint probability by P(B)=0.25.|P(A given B)=0.2/0.25=0.8.', 'D4.1': 'Multiply each value by its probability.|E(X)=2×0.4+7×0.6.|Add 0.8+4.2=5.', 'D4.2': 'For a binomial variable Var(X)=np(1−p).|Substitute n=20 and p=0.25.|20×0.25×0.75=3.75.', 'D4.3': 'Standardize using z=(x−μ)/σ.|Substitute x=80, μ=70, σ=5.|z=(80−70)/5=2.', 'D4.4': 'Adding 5 does not change variance.|Multiplying by 2 multiplies variance by 2².|Var(2X+5)=4×9=36.', 'D5.1': 'To convert a proportion into a percentage, multiply by 100.|Compute 0.04×100.|The p-value is 4%.', 'D5.2': 'An independence test has degrees of freedom (r−1)(c−1).|Substitute r=3 and c=4.|(3−1)(4−1)=2×3=6.', 'D5.3': 'Keep group 1 minus group 2 in the stated order.|Subtract the second mean from the first.|23−19=4.', 'D5.4': 'The margin of error is half the interval width.|The width is 26−18=8.|The margin is 8/2=4.', 'E1.1': 'Differentiate x² to obtain 2x.|Evaluate at x=4.|The gradient is 2×4=8.', 'E2.1': 'Differentiate 3x²+2x−7 to obtain 6x+2.|Evaluate at x=2.|6×2+2=14.', 'E2.2': 'Apply the chain rule: y′=3(2x+1)²×2.|At x=1 this is 6×3².|The derivative value is 54.', 'E3.1': 'An antiderivative of 3x² is x³.|Evaluate the upper bound minus the lower.|2³−0³=8.', 'E3.2': 'On 0≤x≤3, the upper curve is y=3.|Area=∫₀³(3−x)dx=[3x−x²/2]₀³.|9−4.5=4.5 square units.', 'E4.1': 'Differentiate x²−8x+20 to obtain 2x−8.|Set 2x−8=0.|x=4; the positive quadratic coefficient confirms a minimum.', 'E4.2': 'For constant velocity, displacement is velocity×time.|Use 3 m/s for 4 s.|The displacement is 12 m.', 'E4.3': 'First derivative of x³ is 3x².|Second derivative is 6x.|At x=2, f″(2)=12.', 'E5.1': 'Differentiate y=5e⁰·¹ᵗ to get y′=0.5e⁰·¹ᵗ.|At t=0 the exponential is 1.|y′(0)=0.5.', 'E5.2': 'At the initial point the slope is 2y=2×3=6.|One Euler increment is h×slope=0.1×6=0.6.|The updated estimate is 3+0.6=3.6.'}
NUMERIC_SOLUTIONS.update({'A1.3':'Set 4x−8=12 to find the inverse input.|Then 4x=20.|The inverse value is x=5.','A3.3':'At t=0 the exponential equals 1.|The denominator is 1+3=4.|P(0)=800/4=200.','B5.3':'Multiply A by (0,1) to obtain (0,7).|This equals 7(0,1).|The eigenvalue is 7.','D4.5':'Use standard error=σ/√n.|Substitute σ=15 and n=25.|15/√25=15/5=3.'})
questions=[]
for i,l in enumerate(lessons):
 p=l['practice'];m=l['mc'];prefix='M'+str(i+1).zfill(3)
 questions.append(dict(id=prefix+'N',lesson=l['id'],topic=l['topic'],level='HL' if l['hl'] else 'SL',kind='numeric',marks=2,difficulty='Medium',text=p['question'],answer=p['value'],tolerance=max(1e-7,abs(p['value'])*.001),unit=p['unit'],scheme=NUMERIC_SOLUTIONS[l['id']].split('|'),source='Original independent practice'))
 shift=i%4
 rotated=m['options'][shift:]+m['options'][:shift]
 correct=(m['correct']-shift)%4
 questions.append(dict(id=prefix+'C',lesson=l['id'],topic=l['topic'],level='HL' if l['hl'] else 'SL',kind='mcq',marks=1,difficulty='Easy',text=m['question'],options=rotated,correct=correct,scheme=[m['why']],source='Original independent practice'))
# Independent extended tasks, manually marked: mathematical reasoning cannot be inferred from a number alone.
extended=[
 ('A2','A2.2',False,'A ball has height h(t)=−5t²+20t+1. Find its initial height, the time and value of its maximum, and when it first reaches the ground. Explain the valid time domain.',6,['Initial height 1 m.','Vertex time 2 s, maximum 21 m.','Positive root (20+√420)/10 ≈4.05 s.','Use 0≤t≤4.05; the negative root is outside the flight.']),
 ('B3','B3.1',False,'Compare €2000 invested for 4 years at 3% simple interest with 3% compound interest annually. Show both balances and the difference.',5,['Simple balance 2000(1+0.03×4)=€2240.','Compound balance 2000(1.03)^4≈€2251.02.','Compound earns approximately €11.02 more.']),
 ('C3','C3.1',False,'A triangular field has sides 40 m and 60 m with included angle 35°. Find its area and third side. State a practical limitation of the planar model.',6,['Area=0.5×40×60×sin35°≈688.292 m².','Third side=√(40²+60²−2×40×60cos35°)≈35.6100 m.','Assumes a level plane and straight boundaries; a sloping field can differ.']),
 ('D2','D2.1',False,'A study finds a strong positive correlation between hours of exercise and well-being. Explain why this does not establish causation. Give two possible confounders and describe a better study design.',5,['Association alone does not establish direction or eliminate confounding.','Potential confounders include health status, income, sleep or social support.','A feasible randomized or carefully controlled longitudinal design can improve causal inference, with suitable ethics.']),
 ('D4','D4.2',False,'A machine independently produces faulty items with probability 0.08. For 12 items, state a distribution and calculate P(X=0), P(X≥2), and the expected number faulty.',6,['X~B(12,0.08), assuming independent constant-rate trials.','P(X=0)=0.92^12≈0.367666.','P(X≥2)=1−P(X=0)−P(X=1)≈0.248682.','E(X)=12×0.08=0.96.']),
 ('E4','E4.1',False,'A rectangular enclosure uses 40 m of fence for all four sides. Model its area in terms of one side, state the domain, and justify the maximum area.',6,['Let sides be x and 20−x, with 0<x<20.','A=20x−x².','A′=20−2x=0 gives x=10.','A″=−2 confirms a maximum; A=100 m².']),
 ('B5','B5.2',True,'For the column-stochastic matrix with columns (0.8,0.2) and (0.3,0.7), find the stationary probabilities and interpret them.',5,['Let stationary vector be (p,1−p).','p=0.8p+0.3(1−p), so 0.5p=0.3.','p=0.6; vector=(0.6,0.4).','Under suitable transition conditions, proportions approach 60% and 40%.']),
 ('C5','C5.1',True,'A graph has AB=2, AC=5, BC=1, BD=4, CD=2. Find a minimum spanning tree, its weight and a shortest route from A to D. Explain why the two tasks differ.',6,['Choose BC=1, AB=2, CD=2: all four vertices connected without cycles.','Minimum tree weight 5.','Shortest A-B-C-D route also has weight 5 in this graph.','A spanning tree connects all vertices; a shortest path connects only its endpoints. Coinciding totals here do not make the problems identical.']),
 ('E4','E4.2',True,'Velocity v(t)=t−2 for 0≤t≤5. Find displacement and total distance, showing the split at the change of direction.',5,['Velocity changes sign at t=2.','Displacement=[t²/2−2t]₀⁵=2.5.','Distance=|∫₀²(t−2)dt|+|∫₂⁵(t−2)dt|=2+4.5=6.5.']),
 ('E5','E5.2',True,'Apply Euler’s method to y′=y−t, y(0)=1, step h=0.2, to estimate y(0.4). Show each slope and explain one limitation.',6,['First slope=1−0=1, so y(0.2)≈1.2.','Second slope=1.2−0.2=1, so y(0.4)≈1.4.','The result is a step-based approximation; error can accumulate and depends on step size.'])]
for i,(topic,lesson,hl,text,marks,scheme) in enumerate(extended):questions.append(dict(id='MX'+str(i+1).zfill(2),lesson=lesson,topic=topic,level='HL' if hl else 'SL',kind='written',marks=marks,difficulty='Hard',text=text,scheme=scheme,source='Original independent practice'))
names={'A1':'Representation of functions','A2':'Polynomial functions','A3':'Functions with asymptotes','A4':'Trigonometric functions','A5':'Piecewise functions','A6':'Transformations of graphs and functions','B1':'Approximation and error','B2':'Sequences','B3':'Use of technology applications','B4':'Exponentials','B5':'Matrices','C1':'Straight line geometry','C2':'Surface areas, volumes and circles','C3':'Trigonometry and applications','C4':'Vectors','C5':'Graph theory','D1':'Univariate data','D2':'Bivariate data','D3':'Probability','D4':'Probability distributions','D5':'Inferential statistics','E1':'Principles of differential calculus','E2':'Techniques of differential calculus','E3':'Techniques of integral calculus','E4':'Problem-solving using calculus','E5':'Differential equations'}
course=dict(edition='First assessment 2029',basis='IB official 2029 subject brief and curriculum update; full uploaded guide not available for outcome-level verification.',checked='2026-11-09',source='https://ibo.org/globalassets/new-structure/programmes/dp/pdfs/sb_maths_application_en.pdf',updates='https://ibo.org/university-admission/latest-curriculum-updates/dp-mathematics-applications-and-interpretation-updates/',topics=[dict(id=k,name=v,group={'A':'Functions','B':'Number and algebra','C':'Geometry','D':'Probability and statistics','E':'Calculus'}[k[0]],hl=k in ['A6','B5','C4','C5','E5']) for k,v in names.items()],lessons=lessons,questions=questions)
(ROOT/'content/math/course.json').write_text(json.dumps(course,ensure_ascii=False,indent=2))
(ROOT/'dist/maths-data.js').write_text('/* Original independent Maths AI lessons and practice. See SOURCES_2029.md. */\nconst MATHS='+json.dumps(course,ensure_ascii=False,separators=(',',':'))+';\n')
assert set(names)=={l['topic'] for l in lessons}
assert len({q['id'] for q in questions})==len(questions)
print(len(lessons),'Maths lessons;',len(questions),'questions;',len(names),'2029 subject-brief subtopics')

video_map=json.loads((ROOT/"content/math/videos.json").read_text())
assert set(video_map)=={l["id"] for l in lessons}
# Revision videos must remain free and link to an approved public lesson host.
from urllib.parse import urlparse
free_video_hosts={'www.khanacademy.org','en.khanacademy.org','www.youtube.com','addvancemaths.com','www.cs.cornell.edu','mathforcollege.com'}
for lesson_id, resources in video_map.items():
    assert resources, f'No free video for {lesson_id}'
    for video in resources:
        assert video.get('access')=='free', f'Video must be free: {lesson_id}'
        assert urlparse(video['url']).hostname in free_video_hosts, f'Unreviewed video provider: {lesson_id}'

(ROOT/"dist/maths-videos.js").write_text("const MATH_LESSON_VIDEOS="+json.dumps(video_map,ensure_ascii=False,separators=(",",":"))+";\n")
