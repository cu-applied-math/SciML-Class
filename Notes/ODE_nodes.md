---
previewWebRootPath: https://github.com/stephenbeckr/numerical-analysis-class/blob/master/
---
# Supplement on ODEs
Taken from  [APPM/MATH 4650 Intermediate Numerical Analysis](https://github.com/stephenbeckr/numerical-analysis-class/blob/master/syllabus.md#detailed-list-of-topics), taught Fall 2020 by Stephen Becker. In Canvas I will post a link to the youtube playlist for these videos.  *It is not required to watch these videos for the SciML class*, but I'm posting them for students who didn't take the prerequisite numerical analysis class.

- "Introduction to ODEs" (44 min; [Ch5_IntroToODEs.pdf](/Notes/Ch5_IntroToODEs.pdf)), putting them in context (we did *not* discuss DAE; see [Ch5_ODE_resources.md](/Notes/Ch5_ODE_resources.md) for a brief discussion we did later), ch 5.1 (ODE theory) and misc.
  - Demo: [Ch4_ImproperIntegrals.ipynb](/Demos/Ch4_ImproperIntegrals.ipynb)
  - We are *not* covering PDEs, implicit ODEs, nor [DAEs](https://en.wikipedia.org/wiki/Differential-algebraic_system_of_equations), but we are covering *systems of ODEs*
- "Euler's Method" (2 videos, intro and error analysis, 10 and 35 min; [Ch5_EulersMethod.pdf](/Notes/Ch5_EulersMethod.pdf)), ch 5.2
  - Demo: [Ch5_ODEs.ipynb](/Demos/Ch5_ODEs.ipynb)
- "Systems of ODEs" (32 min; [Ch5_SystemsOfODEs.pdf](/Notes/Ch5_SystemsOfODEs.pdf)), ch 5.9
  - Demo: [Ch5_EulersMethod.ipynb](/Demos/Ch5_EulersMethod.ipynb)
- "Higher-order Taylor Methods" and local truncation error (26 min; [Ch5_HigherOrderTaylorMethods.pdf](/Notes/Ch5_HigherOrderTaylorMethods.pdf)), ch 5.3
  - Demo: [Ch5_SystemsOfODEs.ipynb](/Demos/Ch5_SystemsOfODEs.ipynb)
- "Intro to Runge Kutta" (2 videos, 23 min and 9 min; [Ch5_RungeKutta_intro.pdf](/Notes/Ch5_RungeKutta_intro.pdf)), ch 5.4
  - No demo, but we went over [Ch5_ODE_resources.md](/Notes/Ch5_ODE_resources.md)
- "More Runge Kutta" (2 videos, 18 and 15 min; [Ch5_RungeKutta_part2.pdf](/Notes/Ch5_RungeKutta_part2.pdf)), still ch 5.4, adding in lots of Driscoll and Braun
  - Demo: [Ch5_RungeKutta.ipynb](/Demos/Ch5_RungeKutta.ipynb)
- "Adaptive Runge Kutta" and Runge Kutta Fehlberg (29 min; [Ch5_AdaptiveRK.pdf](/Notes/Ch5_AdaptiveRK.pdf)), ch 5.5 and lots of Driscoll and Braun
  - Demo: [Ch5_OrbitDemo.ipynb](/Demos/Ch5_OrbitDemo.ipynb) on [Verlet integration](https://en.wikipedia.org/wiki/Verlet_integration)
- "Multistep methods" and predictor-corrector (2 videos, 19 min and 7 min; [Ch5_MultistepMethods.pdf](/Notes/Ch5_MultistepMethods.pdf))
  - No demo
- "Adaptive multistep methods and extrapolation" (15 min; [Ch5_AdaptiveMultistepMethods_and_Extrapolation.pdf](/Notes/Ch5_AdaptiveMultistepMethods_and_Extrapolation.pdf)), ch 5.7 and 5.8; as you can tell from the short video, we're not emphasizing this material much
  - Demo: [Ch5_MultistepMethods.ipynb](/Demos/Ch5_MultistepMethods.ipynb)
- "Stability", definitions of consistency/convergence/stability, and stability/convergence of one-step methods (2 videos, 23 min and 18 min; [Ch5_Stability_1_definitionsOneStep.pdf](/Notes/Ch5_Stability_1_definitionsOneStep.pdf)), ch 5.10
  - Demo: [Ch5_MultistepMethods_implicit.ipynb](/Demos/Ch5_MultistepMethods_implicit.ipynb) continuing what we did last demo but using Newton's method and others to solve implicit update
- "Stability of multistep methods" and the characteristic polynomial (40 min; [Ch5_Stability_2_multistep.pdf](/Notes/Ch5_Stability_2_multistep.pdf)), ch 5.10 continued
- "Stability Examples" (30 min; [Ch5_Stability_3_examples.pdf](/Notes/Ch5_Stability_3_examples.pdf))
  - Demo: [Ch5_Stability.ipynb](/Demos/Ch5_Stability.ipynb)
- "Stiff Equations and Absolute Stability, part 1 and 2" (25 min and 19 min, [Ch5_Stability_4_stiff_absoluteStability.pdf](/Notes/Ch5_Stability_4_stiff_absoluteStability.pdf)), ch 5.11
  - Demo: [Ch5_AbsoluteStability.ipynb](/Demos/Ch5_AbsoluteStability.ipynb)
