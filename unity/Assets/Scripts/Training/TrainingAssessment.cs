using System;
using System.Collections.Generic;
using UnityEngine;

namespace ARSuraksha.Training
{
    [Serializable]
    public class AssessmentStep
    {
        public string actionId;
        public bool required;
        public bool completed;
    }

    public class TrainingAssessment : MonoBehaviour
    {
        [SerializeField] private string moduleName = "Fire Safety";
        [SerializeField] private int passingScore = 70;

        private readonly List<AssessmentStep> steps = new();

        public void RegisterStep(string actionId, bool required)
        {
            steps.Add(new AssessmentStep
            {
                actionId = actionId,
                required = required,
                completed = false
            });
        }

        public void CompleteStep(string actionId)
        {
            AssessmentStep step = steps.Find(s => s.actionId == actionId);
            if (step != null)
                step.completed = true;
        }

        public int CalculateScore()
        {
            if (steps.Count == 0)
                return 0;

            int completed = 0;
            foreach (AssessmentStep step in steps)
            {
                if (step.completed)
                    completed++;
            }

            return Mathf.RoundToInt((completed / (float)steps.Count) * 100f);
        }

        public bool HasPassed()
        {
            return CalculateScore() >= passingScore;
        }

        public string GetResult()
        {
            int score = CalculateScore();
            return $"{moduleName}: {score}/100 — {(score >= passingScore ? "PASS" : "FAIL")}";
        }
    }
}
