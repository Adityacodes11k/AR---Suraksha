using System;

namespace ARSuraksha.Offline
{
    [Serializable]
    public class TrainingRecord
    {
        public string deviceAttemptId;
        public string workerId;
        public string module;
        public int score;
        public bool passed;
        public string completedAt;
        public bool synced;
    }
}
